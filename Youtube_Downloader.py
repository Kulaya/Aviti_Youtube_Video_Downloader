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

def download_video(url, download_path):
    st.write("Downloading...")
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
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
        # Select the download location using a file dialog
        download_path = st.sidebar.selectbox("Select download location", os.listdir(path=os.path.expanduser("~")))
        if download_path:
            download_path = os.path.join(os.path.expanduser("~"), download_path)
            download_video(url, download_path)
        else:
            st.warning("No download location selected.")
