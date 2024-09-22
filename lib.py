"""functions for m3u8 and mp4"""

import tempfile
import os
import yt_dlp
import m3u8
import mp4

def getVideoType(url):
    """Determine video type (MP4 or M3U8) and download accordingly."""
    _, extension = os.path.splitext(url)
    print(f"File extension: {extension}")
    
    if extension == '.m3u8':
        return m3u8.download_with_ffmpeg(url)  # Return path to video
    
    return mp4.download_video_mp4(url)  # Return path to video

def get_cookies_from_chrome():
    """Use yt-dlp to extract cookies from the logged-in Chrome session."""
    
    ydl_opts = {
        'cookiesfrombrowser': 'chrome',  # This is the official way to extract cookies from Chrome
    }

    # Use a temporary file to store the cookies
    with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as tmp_file:
        cookies_file = tmp_file.name  # Path to the temporary cookies file

    # Use yt-dlp to extract cookies automatically by downloading a dummy video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download(['about:blank'])  # Use a dummy URL to extract cookies
            print(f"Cookies have been extracted and saved to {cookies_file}")
        except Exception as e:
            print(f"Error extracting cookies: {e}")
            return None

    return cookies_file  # Return the path to the cookies file

def checkFileExists(save_path, output_file):
    """Ensure a unique filename by appending numbers if the file already exists."""
    full_output_path = os.path.join(save_path, output_file)
    base, ext = os.path.splitext(full_output_path)
    counter = 1
    new_output_path = full_output_path

    # Generate a unique filename by appending a number if the file already exists
    while os.path.exists(new_output_path):
        new_output_path = f"{base}_{counter}{ext}"
        counter += 1
    
    return new_output_path
