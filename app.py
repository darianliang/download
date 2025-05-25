import os
import webview
import shutil
from yt_dlp import YoutubeDL

class Api:
    def download(self, url, format):
        try:
            if not url:
                return "no url provided"
            
            desktop_path = os.path.expanduser("~/Desktop")
            ffmpeg_path = shutil.which("ffmpeg")
            if not ffmpeg_path:
                ffmpeg_path = "/usr/local/bin/ffmpeg"

            ydl_opts = {
                'outtmpl': os.path.join(desktop_path, '%(title)s.%(ext)s'),
                'cookiefile': 'cookies.txt',
            }

            if format == 'mp3':
                ydl_opts.update({
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                    'ffmpeg_location': ffmpeg_path,
                    'quiet': True,
                })
            elif format == 'mp4':
                ydl_opts.update({
                    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
                    'merge_output_format': 'mp4',
                    'quiet': True,
                    'ffmpeg_location': ffmpeg_path
                })

            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                return f"DOWNLOADED {info.get('title', 'Unknown')}.{format}"
        except Exception as e:
            return f"{str(e)}"


api = Api()
window = webview.create_window('DOWNLOAD', 'gui.html', js_api=api)
webview.start()
