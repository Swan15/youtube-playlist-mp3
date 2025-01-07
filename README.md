# YouTube Playlist to MP3 Downloader

A Streamlit web application that allows users to download entire YouTube playlists as MP3 files. The app converts videos to MP3 format and packages them into a convenient ZIP file for download.

## Features

- Convert entire YouTube playlists to MP3 files
- Simple, user-friendly web interface
- Progress tracking for downloads
- Automatic ZIP file creation
- High-quality audio extraction (192kbps)

## Prerequisites

Before running this application, you need to have Python installed on your system along with FFmpeg.

### FFmpeg Installation

- **Windows**: Download from [FFmpeg website](https://ffmpeg.org/download.html) or install via Chocolatey:
  ```bash
  choco install ffmpeg
  ```
- **macOS**: Install via Homebrew:
  ```bash
  brew install ffmpeg
  ```
- **Linux**: Install via package manager:

  ```bash
  # Ubuntu/Debian
  sudo apt install ffmpeg

  # Fedora
  sudo dnf install ffmpeg
  ```

## Installation

1. Clone this repository:

   ```bash
   git clone [your-repository-url]
   cd [repository-name]
   ```

2. Install required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

   Or install packages individually:

   ```bash
   pip install streamlit yt-dlp
   ```

## Usage

1. Start the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Open your web browser to the provided URL (typically http://localhost:8501)

3. Paste a YouTube playlist URL into the input field

4. Click "Convert to MP3" and wait for the conversion to complete

5. Download the ZIP file containing your MP3s

## Important Notes

- This tool is for personal use only
- Respect copyright and YouTube's terms of service
- Download speed depends on your internet connection and playlist size
- Large playlists may take significant time to process

## License

Use it, don't use it, sell it, I don't give a shit.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions for improvements.

## Disclaimer

This tool is for educational purposes only. Users are responsible for complying with local laws and YouTube's terms of service regarding content downloading.
