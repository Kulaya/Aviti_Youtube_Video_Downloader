import streamlit as st
import pytube
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
            # Show loading spinner
            with st.spinner("Downloading..."):
                # Download the video
                download_video(url, path)
                # Clear the spinner
                st.spinner()

if __name__ == '__main__':
    main()
