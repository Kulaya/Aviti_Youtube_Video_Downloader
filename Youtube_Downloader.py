import streamlit as st
import pytube
import os
from pathlib import Path

# Set the Downloads folder path
DOWNLOADS_PATH = Path.home() / "Downloads"

# Extract video ID from YouTube URL
def extract_video_id(url):
    video_id = pytube.extract.video_id(url)
    return video_id

# Streamlit app
def main():
    st.title("YouTube Video Downloader")

    # Input field for YouTube video URL
    video_url = st.text_input("Enter YouTube Video URL")

    if st.button("Download"):
        if video_url:
            # Extract video ID from URL
            video_id = extract_video_id(video_url)

            if video_id:
                # Download the video
                try:
                    st.text("Downloading...")
                    yt = pytube.YouTube(video_id)
                    stream = yt.streams.first()
                    file_path = DOWNLOADS_PATH / stream.default_filename
                    stream.download(output_path=str(DOWNLOADS_PATH))

                    st.success("Download complete!")
                    st.text(f"Video saved to: {file_path}")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
            else:
                st.warning("Please enter a valid YouTube video URL.")
        else:
            st.warning("Please enter a YouTube video URL.")

# Run the Streamlit app
if __name__ == "__main__":
    main()
