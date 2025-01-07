import streamlit as st
import yt_dlp
import os
import zipfile
import io
import tempfile
import shutil

st.title("YouTube Playlist to MP3 Downloader")
st.write("Enter a YouTube playlist URL to convert and download all videos as MP3 files.")

def download_playlist_as_mp3(playlist_url):
    # Create a temporary directory for downloads
    temp_dir = tempfile.mkdtemp()
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(temp_dir, '%(title)s.%(ext)s'),
        'quiet': True,
        'noplaylist': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract playlist info first
            playlist_info = ydl.extract_info(playlist_url, download=False)
            total_files = len(playlist_info['entries'])
            
            # Create a progress bar
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Download each video with progress updates
            for i, entry in enumerate(playlist_info['entries'], 1):
                status_text.text(f"Downloading {i}/{total_files}: {entry['title']}")
                ydl.download([entry['webpage_url']])
                progress_bar.progress(i/total_files)
        
        # Create a ZIP file in memory
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for file in os.listdir(temp_dir):
                if file.endswith('.mp3'):
                    file_path = os.path.join(temp_dir, file)
                    zip_file.write(file_path, file)
        
        # Clean up the temporary directory
        shutil.rmtree(temp_dir)
        
        return zip_buffer.getvalue()
        
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        return None

# Create the main interface
playlist_url = st.text_input("YouTube Playlist URL", placeholder="https://www.youtube.com/playlist?list=...")

if st.button("Convert to MP3"):
    if playlist_url:
        with st.spinner("Processing playlist... This may take a while depending on the playlist size."):
            zip_data = download_playlist_as_mp3(playlist_url)
            if zip_data:
                st.success("Conversion completed! Click below to download.")
                st.download_button(
                    label="Download MP3s (ZIP)",
                    data=zip_data,
                    file_name="playlist_mp3s.zip",
                    mime="application/zip"
                )
    else:
        st.warning("Please enter a valid YouTube playlist URL") 