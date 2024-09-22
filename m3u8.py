import lib
import subprocess

def download_with_ffmpeg(m3u8_url):
    try:
        print("inside ffmpeg")
        output_file = 'output_file.mp4'
        save_path = lib.get_downloads_folder() or './'
        new_output_path = lib.checkFileExists(save_path, output_file)

        command = [
            'ffmpeg',
            '-i', m3u8_url,
            '-c', 'copy',
            new_output_path
        ]

        subprocess.run(command, check=True)
        print(f"Video downloaded successfully as {new_output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during video download: {e}")
