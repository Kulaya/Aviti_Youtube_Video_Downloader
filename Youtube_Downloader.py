import streamlit as st
from pytube import YouTube
import os

def download_video(url):
    st.write("Downloading...")
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video.download()
    st.write("Download completed!")

    # Open the downloaded video automatically
    file_path = os.path.join(os.getcwd(), video.default_filename)
    os.startfile(file_path)

st.title("YouTube Video Downloader")

# Get the YouTube video URL from the user
url = st.text_input("Enter the YouTube video URL:")
if url:
    if st.button("Download"):
        download_video(url)
