import subprocess
import lib

def download_with_ffmpeg(m3u8_url):
    try:
        print("inside ffmpeg")
        output_file = 'output_file.mp4'
        save_path = lib.get_downloads_folder() or './'
        
        # New output path (ensuring the file doesn't already exist)
        new_output_path = lib.checkFileExists(save_path, output_file)

        # Construct ffmpeg command
        command = [
            'ffmpeg',  # No need for the full path to ffmpeg, just call it directly
            '-i', m3u8_url,  # Input is the .m3u8 URL
            '-c', 'copy',    # Copy audio and video streams without re-encoding
            new_output_path  # Output file name with unique name if necessary
        ]

        # Run the ffmpeg command
        subprocess.run(command, check=True)
        print(f"Video downloaded successfully as {new_output_path}")

    except subprocess.CalledProcessError as e:
        print(f"Error during video download: {e}")
