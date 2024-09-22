import yt_dlp
import lib
import os

def download_video_mp4(url):
    """Download video using cookies from the Chrome session."""
    try:
        save_path = './'
        output_file = 'output_file.mp4'
        new_output_path = os.path.join(save_path, output_file)  # File path without checking if it exists

        # Get cookies from Chrome
        cookies_file = lib.get_cookies_from_chrome()

        if not cookies_file:
            print("Failed to extract cookies, aborting download.")
            return None

        # yt-dlp options
        ydl_opts = {
            'outtmpl': new_output_path,  # Specify the download path and file name
            'cookiefile': cookies_file,  # Use the cookies extracted from Chrome
        }

        # Initialize yt-dlp with the options
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                # Download the video from the provided URL
                ydl.download([url])
                print(f"Video downloaded successfully to {new_output_path}")
                return new_output_path  # Return the file path
            except Exception as e:
                print(f"Error downloading video: {e}")
                return None

        # Cleanup: Delete the temporary cookies file
        if os.path.exists(cookies_file):
            os.remove(cookies_file)
            print(f"Temporary cookies file {cookies_file} deleted")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
