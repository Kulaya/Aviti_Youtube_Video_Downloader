import os
import webbrowser
import streamlit as st
from pytube import YouTube

def download_video(url):
    try:
        st.text('Downloading...')
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        file_path = stream.download()
        st.success('Download completed!')
        return file_path
    except Exception as e:
        st.error(f'Download failed: {str(e)}')

def open_file_location(file_path):
    try:
        file_dir = os.path.dirname(file_path)
        webbrowser.open(file_dir)
    except Exception as e:
        st.error(f'Error opening file location: {str(e)}')

def main():
    st.title('YouTube Video Downloader')
    st.write('Enter the URL of the YouTube video you want to download:')
    
    url = st.text_input('URL')
    
    if st.button('Download'):
        if url:
            file_path = download_video(url)
            if file_path:
                st.success('Download completed!')
                if st.button('Open Downloaded Video'):
                    open_file_location(file_path)
        else:
            st.warning('Please enter a valid YouTube video URL.')

if __name__ == '__main__':
    main()
