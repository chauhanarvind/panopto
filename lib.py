import yt_dlp
import tempfile
import os

def getVideoType(url):
    """Determine video type (MP4 or M3U8) and download accordingly."""
    _, extension = os.path.splitext(url)
    print(f"File extension: {extension}")
    
    if extension == '.m3u8':
        return download_with_ffmpeg(url, True)  # Return path to video
    else:
        return download_video_mp4(url)  # Return path to video

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
