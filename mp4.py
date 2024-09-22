import lib
import yt_dlp

def download_video_mp4(url):
    """Download video using cookies from the Chrome session."""
    try:
        # Get the save path for the download, or use the current directory if none found
        save_path = lib.get_downloads_folder() or './'
        new_output_path = lib.checkFileExists(save_path, 'output.mp4')  # Ensure unique file name

        # Get cookies from Chrome
        cookies_file = lib.get_cookies_from_chrome()

        if not cookies_file:
            print("Failed to extract cookies, aborting download.")
            return

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
            except Exception as e:
                print(f"Error downloading video: {e}")

        # Cleanup: Delete the temporary cookies file
        if os.path.exists(cookies_file):
            os.remove(cookies_file)
            print(f"Temporary cookies file {cookies_file} deleted")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
