import yt_dlp
import os
import platform
import m3u8
import mp4

def getVideoType(url):
    # Extract the file extension
    _, extension = os.path.splitext(url)

    print(f"File extension: {extension}")
    
    if extension=='.m3u8':
        m3u8.download_with_ffmpeg(url)
    else:
        mp4.download_video_mp4(url)
        
        

    
    

