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

    # Download location
    st.write("Select download location:")
    download_path = st.text_input("Folder path", "")

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
