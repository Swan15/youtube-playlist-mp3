#!/usr/bin/env python3
import sys
import yt_dlp

def download_playlist_as_mp3(playlist_url):
    ydl_opts = {
        'format': 'bestaudio/best',  # Download best audio quality
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Convert to audio
            'preferredcodec': 'mp3',  # Output format is MP3
            'preferredquality': '192',  # Set the quality (192 kbps)
        }],
        'outtmpl': '%(title)s.%(ext)s',  # Output filename template
        'quiet': False,  # Display progress
        'noplaylist': False,  # Download all videos in the playlist
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
        print("\nDownload completed successfully!")
    except Exception as e:
        print(f"\nError occurred: {str(e)}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python download_playlist.py <playlist_url>")
        print("Example: python download_playlist.py https://www.youtube.com/playlist?list=PLAYLIST_ID")
        sys.exit(1)
    
    playlist_url = sys.argv[1]
    print(f"Starting download of playlist: {playlist_url}")
    download_playlist_as_mp3(playlist_url)

if __name__ == "__main__":
    main() 