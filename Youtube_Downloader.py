import streamlit as st
import yt_dlp

# Streamlit app title
st.title("YouTube Video Downloader")

# Input field for the URL
url = st.text_input("Enter video URL:", "")

# Download button
if st.button("Download Video"):
    if url:
        try:
            # Display a message to inform the user that download has started
            st.write("Downloading... Please wait.")
            
            # yt_dlp options (keeping it empty as in the original code)
            ydl_opts = {}
            
            # Download the video
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            # Success message
            st.success("Video Downloaded Successfully!")
            
            # Note about file location
            st.info("The video has been downloaded to your current working directory.")
            
        except Exception as e:
            # Error handling
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a valid YouTube URL")

# Optional: Add some instructions
st.write("""
    Instructions:
    1. Paste a YouTube video URL in the input field above
    2. Click 'Download Video'
    3. Wait for the download to complete
    4. The video will be saved in the same directory as this script
""")
