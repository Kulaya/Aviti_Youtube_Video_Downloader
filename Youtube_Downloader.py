import streamlit as st
from pytube import YouTube

# Set Streamlit app title and layout
st.title("YouTube Video Downloader")
st.sidebar.header("Settings")

# Function to download YouTube video
def download_video(url):
    try:
        st.text("Downloading video...")
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        st.success("Video downloaded successfully!")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# User input for YouTube video URL
video_url = st.sidebar.text_input("Enter YouTube video URL")

# Download button
if st.sidebar.button("Download"):
    if video_url:
        download_video(video_url)
    else:
        st.warning("Please enter a valid YouTube video URL.")
