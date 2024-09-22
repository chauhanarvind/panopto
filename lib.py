import os
import platform
import subprocess
import m3u8
import mp4

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
