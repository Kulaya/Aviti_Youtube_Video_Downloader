import streamlit as st
from pytube import YouTube
import webbrowser
import os

def open_video(video_path):
    webbrowser.open(video_path)

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
        # Get the list of directories in the user's home directory
        directory_list = os.listdir(path=os.path.expanduser("~"))

        # Prepend "Downloads" to the directory list
        directory_list.insert(0, "Downloads")

        # Select the download location using a file dialog
        download_path = st.sidebar.selectbox("Select download location", directory_list)
        if download_path:
            if download_path == "Downloads":
                download_path = os.path.join(os.path.expanduser("~"), "Downloads")
            else:
                download_path = os.path.join(os.path.expanduser("~"), download_path)

            download_video(url, download_path)
        else:
            st.warning("No download location selected.")
