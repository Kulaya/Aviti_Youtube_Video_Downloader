import streamlit as st
from pytube import YouTube
import os

def download_video(url, download_path):
    st.write("Downloading...")
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video_path = os.path.join(download_path, video.default_filename)
    video.download(output_path=download_path)
    st.write("Download completed!")

    # Display button to open the downloaded video
    st.write("Click the button below to open the downloaded video:")
    if st.button("Open Video"):
        open_video(video_path)

def open_video(video_path):
    os.startfile(video_path)  # For Windows

st.title("YouTube Video Downloader")

# Get the YouTube video URL from the user
url = st.text_input("Enter the YouTube video URL:")
if url:
    if st.button("Download"):
        download_path = os.path.join(os.path.expanduser("~"), "Downloads")
        download_video(url, download_path)
