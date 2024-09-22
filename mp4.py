import lib
import yt_dlp

def download_video_mp4(url):
    save_path = lib.get_downloads_folder() or './' 
    new_output_path = lib.checkFileExists(save_path, 'output.mp4')
    
    ydl_opts = {
        'outtmpl': new_output_path  # Directly set the output path
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print(f"Video downloaded successfully to {new_output_path}")
        except Exception as e:
            print(f"Error downloading video: {e}")
