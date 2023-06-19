import streamlit as st
from pytube import YouTube
import os

# Set Streamlit app title and layout
st.title("YouTube Video Downloader")
st.sidebar.header("Settings")

# Function to download YouTube video
def download_video(url, download_path):
    try:
        st.text("Downloading video...")
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        download_folder = os.path.join(download_path, yt.title)
        os.makedirs(download_folder, exist_ok=True)
        stream.download(output_path=download_folder)
        st.success("Video downloaded successfully!")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# User input for YouTube video URL and download path
video_url = st.sidebar.text_input("Enter YouTube video URL")

# Download path selection
download_path = st.sidebar.file_uploader("Select download folder", type="directory")

# Download button
if st.sidebar.button("Download"):
    if video_url and download_path:
        download_video(video_url, download_path)
    else:
        st.warning("Please enter a valid YouTube video URL and select a download folder.")
