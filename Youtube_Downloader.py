import streamlit as st
import pytube
import threading
import os

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

    # Download button
    if st.button("Download"):
        # Get download location
        path = st.file_picker(label="Select download location", type=["directory"])
        if path:
            # Create a separate thread for downloading
            download_thread = threading.Thread(target=download_video, args=(url, path))
            download_thread.start()

if __name__ == '__main__':
    main()
