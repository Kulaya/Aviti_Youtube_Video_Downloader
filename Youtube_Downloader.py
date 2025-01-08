import streamlit as st
import yt_dlp
from pathlib import Path

def download_video(url, output_path):
    try:
        ydl_opts = {
            'outtmpl': str(output_path / '%(title)s.%(ext)s')
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

# File manager dialog to select the destination folder
destination_folder = st.text_input("Select the destination folder:", value=str(Path.home() / "Downloads"))

destination_path = Path(destination_folder)
if not destination_path.exists():
    st.error("The selected folder does not exist. Please enter a valid folder path.")

# Download button
if st.button("Download Video"):
    if video_url and destination_path.exists():
        success, error_message = download_video(video_url, destination_path)
        if success:
            st.success(f"Video downloaded successfully to {destination_path}!")
        else:
            st.error(f"Failed to download video. Error: {error_message}")
    elif not video_url:
        st.warning("Please enter a valid URL.")
    else:
        st.error("Invalid destination folder. Please check the folder path.")
