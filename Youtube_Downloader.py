import streamlit as st
import yt_dlp
import os

def download_video(url, output_path):
    """Download YouTube video to the specified output path."""
    try:
        ydl_opts = {
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s')
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

# Destination folder selection
default_output_path = os.path.join(os.path.expanduser("~"), "Downloads")
output_path = st.text_input(
    "Enter the destination folder:", value=default_output_path
)

# Download button
if st.button("Download Video"):
    if video_url.strip():
        if os.path.isdir(output_path):
            success, error_message = download_video(video_url, output_path)
            if success:
                st.success(f"Video downloaded successfully to {output_path}.")
            else:
                st.error(f"Failed to download video. Error: {error_message}")
        else:
            st.error("Invalid destination folder. Please enter a valid path.")
    else:
        st.error("Please enter a valid video URL.")
