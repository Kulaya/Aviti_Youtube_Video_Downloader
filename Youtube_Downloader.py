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
    download_path = st.text_input("Download location", "", key="download_path")

    # Directory selection dialog
    if st.button("Select location"):
        root = tk.Tk()
        root.withdraw()
        folder_selected = filedialog.askdirectory()
        root.destroy()
        st.session_state.download_path = folder_selected

    # Download button
    if st.button("Download"):
        path = st.session_state.download_path
        if path:
            # Show loading spinner
            with st.spinner("Downloading..."):
                # Download the video
                download_video(url, path)
                # Clear the spinner
                st.spinner()

if __name__ == '__main__':
    main()
