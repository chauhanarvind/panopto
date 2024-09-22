import os
import platform
import subprocess
import m3u8
import mp4
import subprocess
import lib
import yt_dlp
import tempfile
import os

def getVideoType(url):
    _, extension = os.path.splitext(url)
    print(f"File extension: {extension}")
    
    if extension == '.m3u8':
        m3u8.download_with_ffmpeg(url,True)
    else:
        mp4.download_video_mp4(url)

def get_downloads_folder():
    if platform.system() == "Windows":
        return os.path.join(os.environ['USERPROFILE'], 'Downloads')
    else:
        return os.path.join(os.path.expanduser('~'), 'Downloads')

def checkFileExists(save_path, output_file):
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    full_output_path = os.path.join(save_path, output_file)
    base, ext = os.path.splitext(full_output_path)
    counter = 1
    new_output_path = full_output_path

    while os.path.exists(new_output_path):
        new_output_path = f"{base}_{counter}{ext}"
        counter += 1
    
    return new_output_path

def get_cookies_from_chrome():
    """Use yt-dlp to extract cookies from the logged-in Chrome session."""
    ydl_opts = {
        'cookiesfrombrowser': 'chrome',  # Extract cookies from Chrome
    }

    # Use tempfile to create a temporary file for cookies
    with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as tmp_file:
        cookies_file = tmp_file.name  # Get the path to the temporary file

    # Use yt-dlp to extract cookies
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            # Extract cookies and save to a variable
            cookies_data = ydl._get_cookies_from_browser('chrome')
            
            # Write cookies to the cookies.txt file
            with open(cookies_file, 'w') as f:
                for cookie in cookies_data:
                    f.write(f"{cookie.name}\t{cookie.value}\n")

            print(f"Cookies saved to {cookies_file}")

        except Exception as e:
            print(f"Error extracting cookies: {e}")
            return None

    return cookies_file
