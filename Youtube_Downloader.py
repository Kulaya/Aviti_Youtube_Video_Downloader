import streamlit as st
from pytube import YouTube
import os
import tempfile

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

# User input for YouTube video URL
video_url = st.sidebar.text_input("Enter YouTube video URL")

# File uploader for selecting the download folder path
folder_path_file = st.sidebar.file_uploader(
    "Upload a file containing the download folder path",
    type=["txt"],
    accept_multiple_files=False
)

# Download button
if st.sidebar.button("Download"):
    if video_url and folder_path_file is not None:
        folder_path = folder_path_file.getvalue().decode("utf-8").strip()
        download_video(video_url, folder_path)
    else:
        st.warning("Please enter a valid YouTube video URL and select a download folder path.")
