def main():
    st.title("YouTube Video Downloader")
       video_url = st.text_input("Enter the YouTube video URL:")
       download_button = st.button("Download")

       if download_button:
           if video_url:
               try:
                   st.write("Downloading...")
                   yt = YouTube(video_url)
                   stream = yt.streams.get_highest_resolution()
                   stream.download()
                   st.success("Video downloaded successfully!")
               except Exception as e:
                   st.error(f"An error occurred: {str(e)}")
           else:
               st.warning("Please enter a valid YouTube video URL.")

   if __name__ == "__main__":
       main()
