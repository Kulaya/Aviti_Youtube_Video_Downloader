import streamlit as st
import yt_dlp
from tkinter import Tk, filedialog

def browse_destination_folder():
    root = Tk()
    root.withdraw()  # Hide the root window
    folder_selected = filedialog.askdirectory(title="Select Destination Folder")
    root.destroy()  # Destroy the Tkinter root window
    return folder_selected

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
        destination_folder = browse_destination_folder()
        if destination_folder:
            from pathlib import Path
            destination_path = Path(destination_folder)
            success, error_message = download_video(video_url, destination_path)
            if success:
                st.success(f"Video downloaded successfully to {destination_folder}!")
            else:
                st.error(f"Failed to download video. Error: {error_message}")
        else:
            st.warning("No folder selected. Please select a destination folder.")
    else:
        st.warning("Please enter a valid URL.")
