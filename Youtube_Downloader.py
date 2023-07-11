import streamlit as st
import pytube
import os
from urllib.parse import urlparse, parse_qs
from pathlib import Path

# Set the Downloads folder path
DOWNLOADS_PATH = Path.home() / "Downloads"

# Extract video ID from YouTube URL
def extract_video_id(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    video_id = query_params.get("v")
    if video_id:
        return video_id[0]
    return None

# Streamlit app
def main():
    st.title("YouTube Video Downloader")

    # Input field for YouTube video URLs
    video_urls = st.text_area("Enter YouTube Video URLs (one URL per line)", height=200)

    if st.button("Download"):
        if video_urls:
            urls_list = video_urls.split("\n")

            for url in urls_list:
                # Extract video ID from URL
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
