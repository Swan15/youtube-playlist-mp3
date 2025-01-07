import streamlit as st
import yt_dlp
import os

def progress_hook(d):
    if d['status'] == 'downloading':
        try:
            total = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
            downloaded = d.get('downloaded_bytes', 0)
            if total > 0:
                progress = (downloaded / total)
                st.session_state.progress_bar.progress(progress)
                st.session_state.status_text.text(f"Downloading: {d['filename']} - {d.get('_percent_str', '0%')}")
        except Exception:
            pass
    elif d['status'] == 'finished':
        st.session_state.status_text.text(f"Converting {d['filename']} to MP3...")

def download_playlist_as_mp3(playlist_url, download_dir):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'quiet': False,
        'noplaylist': False,
        'progress_hooks': [progress_hook],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
        return True, "Download completed successfully!"
    except Exception as e:
        return False, f"Error occurred: {str(e)}"

st.title('YouTube Playlist Downloader')
st.write('Enter a YouTube playlist URL and download location to download all videos as MP3')

download_dir = st.text_input('Download Directory (full path)', 
                            value=os.path.expanduser('~/Downloads'),
                            help='Enter the full path where you want to save the MP3 files')

url = st.text_input('Playlist URL')
if st.button('Download'):
    if url and download_dir:
        if not os.path.exists(download_dir):
            try:
                os.makedirs(download_dir)
            except Exception as e:
                st.error(f'Could not create download directory: {str(e)}')
                st.stop()
        
        st.session_state.progress_bar = st.progress(0)
        st.session_state.status_text = st.empty()
        
        with st.spinner('Processing...'):
            success, message = download_playlist_as_mp3(url, download_dir)
            if success:
                st.session_state.status_text.text("All downloads completed!")
                st.success(message)
            else:
                st.error(message)
    else:
        st.error('Please enter both a URL and download directory') 