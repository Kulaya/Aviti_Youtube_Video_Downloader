# app.py
import streamlit as st
import yt_dlp
import os
from pathlib import Path

st.title("YouTube Video Downloader")

# Input field for the URL
url = st.text_input("Enter video URL:", "")

# Function to download the video and return the file path
def download_video(url, output_path="downloaded_video"):
    ydl_opts = {
        'outtmpl': f'{output_path}.%(ext)s',  # Save with the video's extension
        'format': 'best',  # Download the best available quality
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    # Find the downloaded file (yt_dlp appends the extension dynamically)
    for file in os.listdir():
        if file.startswith(output_path):
            return file
    return None

# Download button
if st.button("Download Video"):
    if url:
        try:
            st.write("Downloading... Please wait.")
            # Download the video to the server
            downloaded_file = download_video(url)
            
            if downloaded_file and os.path.exists(downloaded_file):
                st.success("Video Downloaded Successfully!")
                # Read the file as binary data
                with open(downloaded_file, "rb") as file:
                    st.download_button(
                        label="Click to Save Video Locally",
                        data=file,
                        file_name=downloaded_file,
                        mime="video/mp4"  # Adjust MIME type as needed
                    )
                # Clean up the file after offering it for download
                os.remove(downloaded_file)
            else:
                st.error("Failed to locate the downloaded video.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a valid YouTube URL")

st.write("Enter a YouTube URL, click 'Download Video', then use the 'Click to Save Video Locally' button to save it to your device.")
