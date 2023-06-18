import streamlit as st
from pytube import YouTube
import webbrowser
import os

def open_video(video_path):
    system = os.name
    if system == "nt":  # Windows
        os.startfile(video_path)
    elif system == "posix":  # macOS or Linux
        opener = "open" if system == "Darwin" else "xdg-open"
        os.system(f"{opener} {video_path}")

def download_video(url):
    st.write("Downloading...")
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    download_path = os.path.join(os.path.expanduser('~'), "Downloads")
    video_path = os.path.join(download_path, video.default_filename)
    video.download(output_path=download_path)
    st.write("Download completed!")

    # Open the downloaded video automatically
    open_video(video_path)

st.title("YouTube Video Downloader")

# Get the YouTube video URL from the user
url = st.text_input("Enter the YouTube video URL:")
if url:
    if st.button("Download"):
        download_video(url)
