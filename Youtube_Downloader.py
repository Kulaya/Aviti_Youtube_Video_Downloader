import streamlit as st
from pytube import YouTube
import os
import subprocess

def download_video(url, download_path):
    st.write("Downloading...")
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video_path = os.path.join(download_path, video.default_filename)
    video.download(output_path=download_path)
    st.write("Download completed!")

    # Open the downloaded video automatically
    st.write("Opening video...")
    open_video(video_path)

def open_video(video_path):
    if os.name == "nt":  # Windows
        os.startfile(video_path)
    elif os.name == "posix":  # macOS or Linux
        subprocess.run(["xdg-open", video_path])

st.title("YouTube Video Downloader")

# Get the YouTube video URL from the user
url = st.text_input("Enter the YouTube video URL:")
if url:
    if st.button("Download"):
        download_path = os.path.join(os.path.expanduser("~"), "Downloads")
        download_video(url, download_path)
