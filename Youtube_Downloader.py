import streamlit as st
import pytube
import os
import re
from pathlib import Path

# Set the Downloads folder path
DOWNLOADS_PATH = Path.home() / "Downloads"

# Extract video ID from YouTube URL using regex
def extract_video_id(url):
    regex_patterns = [
        r"(?:https?:\/\/(?:www\.|m\.|music\.)?youtube\.com\/[^\s/$.?#].[^\s]*)|(?:https?:\/\/(?:www\.|m\.|music\.)?youtube\.com\/[^\s/$.?#]\/[^\s/$.?#]*\/[^\s]*)|(?:https?:\/\/(?:www\.|m\.|music\.)?youtube\.com\/[^\s/$.?#]\/[^\s]*)",
        r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:watch\?v=|.*&v=|embed\/|v\/|shorts\/|.*\/videos\/))(?P<id>[A-Za-z0-9_-]{11})"
    ]
    video_id = None
    for pattern in regex_patterns:
        match = re.search(pattern, url)
        if match and match.group("id"):
            video_id = match.group("id")
            break
    return video_id

# Streamlit app
def main():
    st.title("YouTube Video Downloader")

    # Input field for YouTube video URLs
    video_urls = st.text_area("Enter YouTube Video URLs (one URL per line)", height=200)

    if st.button("Download"):
        if video_urls:
            urls_list = video_urls.split("\n")

            for url in urls_list:
                # Extract video ID from URL using regex
                video_id = extract_video_id(url)

                if video_id:
                    # Download the video
                    try:
                        st.text(f"Downloading {url}...")
                        yt = pytube.YouTube(video_id)
                        stream = yt.streams.first()
                        file_path = DOWNLOADS_PATH / stream.default_filename
                        stream.download(output_path=str(DOWNLOADS_PATH))

                        st.success(f"Download of {url} complete!")
                        st.text(f"Video saved to: {file_path}")
                    except Exception as e:
                        st.error(f"An error occurred while downloading {url}: {str(e)}")
                else:
                    st.warning(f"Invalid YouTube video URL: {url}")

        else:
            st.warning("Please enter at least one YouTube video URL.")

# Run the Streamlit app
if __name__ == "__main__":
    main()
