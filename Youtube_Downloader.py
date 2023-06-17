import os
import streamlit as st
from pytube import YouTube

def download_video(url):
    try:
        st.text('Downloading...')
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        st.success('Download completed!')
    except Exception as e:
        st.error(f'Download failed: {str(e)}')

def main():
    st.title('YouTube Video Downloader')
    st.write('Enter the URL of the YouTube video you want to download:')
    
    url = st.text_input('URL')
    
    if st.button('Download'):
        if url:
            download_video(url)
        else:
            st.warning('Please enter a valid YouTube video URL.')

if __name__ == '__main__':
    main()
