import streamlit as st
import yt_dlp
import os
import platform

if platform.system() == "Windows":
    import ctypes.wintypes
    from win32com.shell import shell, shellcon

def browse_destination():
    if platform.system() == "Windows":
        folder_pidl = shell.SHBrowseForFolder(
            0, None, "Select a folder", shellcon.BIF_RETURNONLYFSDIRS
        )
        if folder_pidl:
            folder_path = shell.SHGetPathFromIDList(folder_pidl)
            return folder_path.decode("utf-8") if isinstance(folder_path, bytes) else folder_path
        return None
    else:
        st.warning("This feature is only supported on Windows.")
        return None

def download_video(url, destination):
    ydl_opts = {
        'outtmpl': os.path.join(destination, '%(title)s.%(ext)s'),  # Save to the selected destination folder
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
