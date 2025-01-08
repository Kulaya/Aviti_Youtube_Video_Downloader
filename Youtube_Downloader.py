import streamlit as st
import yt_dlp
from tkinter import Tk, filedialog

def browse_destination():
    root = Tk()
    root.withdraw()  # Hide the main Tkinter window
    folder_selected = filedialog.askdirectory(title="Select Destination Folder")
    root.destroy()  # Close the Tkinter window
    return folder_selected

def download_video(url, destination):
    ydl_opts = {
        'outtmpl': f'{destination}/%(title)s.%(ext)s',  # Save to the selected destination folder
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Streamlit App Interface
st.title("YouTube Video Downloader")

# Input for YouTube video URL
url = st.text_input("Enter YouTube video URL:")

if st.button("Download Video"):
    if url:
        try:
            st.info("Please select the destination folder.")
            destination = browse_destination()
            if destination:
                st.info("Downloading... Please wait.")
                download_video(url, destination)
                st.success(f"Video downloaded successfully to {destination}!")
            else:
                st.warning("Download canceled. No destination folder selected.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid URL.")
