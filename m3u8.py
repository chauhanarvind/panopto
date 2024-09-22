import subprocess
import os
import lib

def download_with_ffmpeg(m3u8_url, cookies_from_browser=True):
    try:
        print("inside ffmpeg")
        output_file = 'output_file.mp4'
        save_path = './'  # Save to current directory
        new_output_path = os.path.join(save_path, output_file)

        # If cookies are to be extracted from the browser (Chrome), do so
        cookie_header = None
        cookies_file = None
        if cookies_from_browser:
            cookies_file = lib.get_cookies_from_chrome()  # Get cookies from Chrome
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

        # Cleanup: Delete the temporary cookies file if it exists
        if cookies_file and os.path.exists(cookies_file):
            os.remove(cookies_file)
            print(f"Temporary cookies file {cookies_file} deleted")

        return new_output_path  # Return the path to the downloaded video

    except subprocess.CalledProcessError as e:
        print(f"Error during video download: {e}")
        return None

    except Exception as general_error:
        print(f"An unexpected error occurred: {general_error}")
        return None
