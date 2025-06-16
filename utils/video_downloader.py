import yt_dlp
import os
import uuid

DOWNLOAD_DIR = "downloads/"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def download_video(url: str) -> str:
    video_id = str(uuid.uuid4())
    output_path = os.path.join(DOWNLOAD_DIR, f"{video_id}.%(ext)s")

    ydl_opts = {
        "format": "mp4",
        "outtmpl": output_path,
        "quiet": True,
        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        final_path = ydl.prepare_filename(info)

    return final_path
