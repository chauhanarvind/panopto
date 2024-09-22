import lib
import yt_dlp

def download_video_mp4(url):  # Default browser set to Chrome
    browser = 'chrome'
    # Get the save path for the download, or use the current directory if none found
    save_path = lib.get_downloads_folder() or './'
    new_output_path = lib.checkFileExists(save_path, 'output.mp4')  # Ensure unique file name

    # yt-dlp options
    ydl_opts = {
        'outtmpl': new_output_path,  # Specify the download path and file name
        'cookiesfrombrowser': browser  # Use cookies from the default browser session (Chrome)
    }

    # Initialize yt-dlp with the options
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            # Download the video from the provided URL
            ydl.download([url])
            print(f"Video downloaded successfully to {new_output_path}")
        except Exception as e:
            print(f"Error downloading video: {e}")
