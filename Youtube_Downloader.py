import streamlit as st
import pytube
import os
import tkinter as tk
from tkinter import filedialog

def download_video(url, path):
    try:
        st.write("Downloading...")
        youtube = pytube.YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download(path)
        st.write("Download completed!")
    except Exception as e:
        st.write("An error occurred:", str(e))

def main():
    st.title("YouTube Video Downloader")

    # Input URL
    url = st.text_input("Enter YouTube Video URL", "")

    # Download location
    st.write("Select download location:")
    download_path = st.text_input("Folder path", "")
    browse_button = st.button("Browse")

    # Browse folder
    if browse_button:
        root = tk.Tk()
        root.withdraw()
        folder_selected = filedialog.askdirectory()
        root.destroy()
        if folder_selected:
            download_path = folder_selected

    # Download button
    if st.button("Download"):
        if download_path:
            # Show loading spinner
            with st.spinner("Downloading..."):
                # Download the video
                download_video(url, download_path)
                # Clear the spinner
                st.spinner()

if __name__ == '__main__':
    main()
