# app.py
import streamlit as st
import yt_dlp

st.title("YouTube Video Downloader")

# Input field for the URL
url = st.text_input("Enter video URL:", "")

# Download button
if st.button("Download Video"):
    if url:
        try:
            st.write("Downloading... Please wait.")
            ydl_opts = {}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            st.success("Video Downloaded Successfully!")
            st.info("Note: The video is downloaded to the server, not your local machine.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a valid YouTube URL")

st.write("Enter a YouTube URL and click 'Download Video' to download the video.")
