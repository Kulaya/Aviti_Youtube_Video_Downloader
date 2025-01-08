import streamlit as st
import yt_dlp
import os

def download_video(url):
    try:
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        ydl_opts = {
            'outtmpl': os.path.join(downloads_path, '%(title)s.%(ext)s')
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return True, None
    except Exception as e:
        return False, str(e)

# Streamlit app
st.title("YouTube Video Downloader")

# Input for the video URL
video_url = st.text_input("Enter the YouTube video URL:")

# Download button
if st.button("Download Video"):
    if video_url:
        success, error_message = download_video(video_url)
        if success:
            st.success("Video downloaded successfully! Check your Downloads folder.")
        else:
            st.error(f"Failed to download video. Error: {error_message}")
    else:
        st.warning("Please enter a valid URL.")
