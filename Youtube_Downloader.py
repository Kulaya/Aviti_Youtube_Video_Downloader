import streamlit as st
from pytube import YouTube
import platform
import subprocess

def open_video(video_path):
    system = platform.system()
    if system == "Windows":
        subprocess.Popen([video_path], shell=True)
    elif system == "Darwin":  # macOS
        subprocess.Popen(["open", video_path])
    else:  # Linux
        subprocess.Popen(["xdg-open", video_path])

def download_video(url):
    st.write("Downloading...")
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video.download()
    st.write("Download completed!")

    # Open the downloaded video automatically
    open_video(video.default_filename)

st.title("YouTube Video Downloader")

# Get the YouTube video URL from the user
url = st.text_input("Enter the YouTube video URL:")
if url:
    if st.button("Download"):
        download_video(url)
