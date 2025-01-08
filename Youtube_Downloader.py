import streamlit as st
import yt_dlp

def download_video(url):
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Streamlit App Interface
st.title("YouTube Video Downloader")

# Input for YouTube video URL
url = st.text_input("Enter YouTube video URL:")

if st.button("Download Video"):
    if url:
        try:
            st.info("Downloading... Please wait.")
            download_video(url)
            st.success("Video downloaded successfully!")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid URL.")
