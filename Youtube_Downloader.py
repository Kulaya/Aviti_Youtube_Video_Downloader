import streamlit as st
from pytube import YouTube

# Set page title
st.set_page_config(page_title="YouTube Downloader")

# Define function to download YouTube video
def download_video(video_url, video_format):
    try:
        # Create YouTube object
        yt = YouTube(video_url)

        # Get video stream with selected format
        stream = yt.streams.get_by_resolution(video_format)

        # Download video
        stream.download()

        # Display success message
        st.success("Video downloaded successfully!")
    except Exception as e:
        # Display error message
        st.error("An error occurred: " + str(e))

# Page title
st.title("YouTube Downloader")

# Video URL input
video_url = st.text_input("Enter the URL of the YouTube video you want to download:")

# Video format selection
video_format = st.selectbox("Select the video format you want to download:", ["720p", "480p", "360p"])

# Download button
if st.button("Download"):
    if not video_url:
        st.warning("Please enter a valid YouTube video URL.")
    else:
        download_video(video_url, video_format)
