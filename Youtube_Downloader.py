import argparse
from pytube import YouTube

def download_video(url, download_path):
    print("Downloading...")
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video.download(output_path=download_path)
    print("Download completed!")

def main():
    parser = argparse.ArgumentParser(description="YouTube Video Downloader")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("download_path", help="Download location")

    args = parser.parse_args()

    download_video(args.url, args.download_path)

if __name__ == "__main__":
    main()
