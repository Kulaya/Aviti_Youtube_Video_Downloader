import streamlit as st
from pytube import YouTube
import os
import tkinter as tk
from tkinter import filedialog

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

# Button for browsing folder location
def browse_folder():
    root = tk.Tk()
    root.withdraw()
    selected_folder = filedialog.askdirectory()
    download_path_input.text(selected_folder)

browse_button = st.sidebar.button("Browse")
if browse_button:
    browse_folder()

# User input for download folder path
download_path_input = st.sidebar.text_input("Enter download folder path")

# Download button
if st.sidebar.button("Download"):
    if video_url and download_path_input.value:
        download_video(video_url, download_path_input.value)
    else:
        st.warning("Please enter a valid YouTube video URL and download folder path.")
