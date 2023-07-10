import youtube_dl
import streamlit as st

def download_video(url, format, quality):
    try:
        # Set the options for downloading the video
        options = {
            'format': format,
            'outtmpl': '~/Downloads/%(title)s.%(ext)s',
            'quiet': True,
        }

        # Add the requested quality if specified
        if quality:
            options['format'] += f'+{quality}'

        # Create a YouTubeDL object
        ydl = youtube_dl.YoutubeDL(options)

        # Download the video
        with ydl:
            result = ydl.extract_info(url, download=True)

        st.success("Video downloaded successfully!")
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Streamlit application
st.title("YouTube Video Downloader")

# Input fields
video_url = st.text_input("Enter YouTube video URL")
format = st.selectbox("Select format", ['bestvideo+bestaudio/best', 'bestvideo', 'bestaudio'])
quality = st.selectbox("Select quality", ['1080p', '720p', '480p', '360p', '240p', '144p'])
download_button = st.button("Download")

# Perform download when Download button is clicked
if download_button:
    if video_url:
        download_video(video_url, format, quality)
    else:
        st.warning("Please enter a YouTube video URL.")
