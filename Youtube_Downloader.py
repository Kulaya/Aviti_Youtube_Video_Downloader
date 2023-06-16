import streamlit as st
from pytube import YouTube

def download_video(url, output_path):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()  # Get the highest resolution stream
        video.download(output_path)
        return "Download completed successfully!"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit application
st.title("YouTube Video Downloader")

# Input fields
video_url = st.text_input("Enter the YouTube video URL", "")

# Output directory selection
output_directory = st.text_input("Enter the output directory path", "")
output_directory = st.text_input("Enter the output directory path", "")

# Browse button to select output directory
if st.button("Browse"):
    output_directory = st.file_dialog("Select output directory", type=1)

# Download button
if st.button("Download"):
    if video_url and output_directory:
        st.text("Downloading...")
        result = download_video(video_url, output_directory)
        st.text(result)
    else:
        st.warning("Please provide a video URL and output directory path.")
