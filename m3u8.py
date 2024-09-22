import subprocess
import lib
import yt_dlp

def get_cookies_from_chrome():
    """Use yt-dlp to extract cookies from the logged-in Chrome session."""
    ydl_opts = {
        'cookiesfrombrowser': 'chrome',  # Extract cookies from Chrome
    }

    # Temporary file to save cookies
    cookies_file = '/tmp/cookies.txt'

    # Use yt-dlp to save the cookies to a file
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            # This is a hack: yt-dlp normally expects to download something
            # but here we are just using it to get cookies.
            # So we invoke it on a simple URL like 'about:blank'.
            ydl.download(['about:blank'])
        except Exception:
            pass  # We ignore the exception because we're just using it to get cookies

    return cookies_file

def download_with_ffmpeg(m3u8_url, cookies_from_browser=True):
    try:
        print("inside ffmpeg")
        output_file = 'output_file.mp4'
        save_path = lib.get_downloads_folder() or './'
        
        # New output path (ensuring the file doesn't already exist)
        new_output_path = lib.checkFileExists(save_path, output_file)

        # If cookies are to be extracted from the browser (Chrome), do so
        cookie_header = None
        if cookies_from_browser:
            cookies_file = get_cookies_from_chrome()  # Get cookies from Chrome
            if cookies_file:
                with open(cookies_file, 'r') as file:
                    cookie_header = file.read()

        # Construct ffmpeg command with cookies (if provided)
        command = [
            'ffmpeg',  # ffmpeg executable
            '-i', m3u8_url,  # Input .m3u8 URL
            '-c', 'copy',  # Copy audio and video streams without re-encoding
            new_output_path  # Output file name
        ]

        # If cookies are available, add them as headers
        if cookie_header:
            command.insert(1, '-headers')
            command.insert(2, f"Cookie: {cookie_header}")

        # Run the ffmpeg command
        subprocess.run(command, check=True)
        print(f"Video downloaded successfully as {new_output_path}")

    except subprocess.CalledProcessError as e:
        print(f"Error during video download: {e}")
