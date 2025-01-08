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

# Download button
if st.button("Download Video"):
    if video_url:
        st.info("Please select the destination folder.")
        destination_folder = st.text_input("Enter the destination folder path:")
        if destination_folder:
            destination_path = Path(destination_folder)
            if destination_path.exists() and destination_path.is_dir():
                success, error_message = download_video(video_url, destination_path)
                if success:
                    st.success(f"Video downloaded successfully to {destination_folder}!")
                else:
                    st.error(f"Failed to download video. Error: {error_message}")
            else:
                st.error("The entered path is not a valid folder. Please try again.")
        else:
            st.warning("No folder entered. Please enter a valid destination folder path.")
    else:
        st.warning("Please enter a valid URL.")
