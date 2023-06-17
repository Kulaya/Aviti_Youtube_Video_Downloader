import streamlit as st
from pytube import YouTube
import os

def download_video(url, output_path):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()  # Get the highest resolution stream
        video.download(output_path)
        return "Download completed successfully!"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit application
st.title("YouTube Video Downloader")

# Input fields
video_url = st.text_input("Enter the YouTube video URL", key="video_url")

# Output directory selection
output_directory = st.sidebar.empty()

# Browse button
if st.sidebar.button("Browse"):
    output_directory_path = st.sidebar.file_uploader("Select output directory", type=None, key="output_directory")
    if output_directory_path is not None:
        output_directory_path = output_directory_path.name
        output_directory.info(f"Output directory: {output_directory_path}")
    else:
        output_directory.warning("Please select an output directory.")

# Download button
if st.button("Download"):
    if video_url and output_directory_path:
        st.text("Downloading...")
        result = download_video(video_url, output_directory_path)
        st.text(result)
    else:
        st.warning("Please provide a video URL and select an output directory.")
