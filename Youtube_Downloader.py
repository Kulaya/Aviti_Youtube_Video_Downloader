import streamlit as st
import yt_dlp

def download_video(url):
    try:
        ydl_opts = {}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return True
    except Exception as e:
        return False, str(e)

# Streamlit app
st.title("YouTube Video Downloader")

# Input for the video URL
video_url = st.text_input("Enter the YouTube video URL:")

# Download button
if st.button("Download Video"):
    if video_url:
        success = download_video(video_url)
        if success:
            st.success("Video Downloaded Successfully!")
        else:
            st.error(f"Failed to download video. {success[1]}")
    else:
        st.warning("Please enter a valid URL.")
