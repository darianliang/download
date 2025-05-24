import webview
import yt_dlp
import os

class API:
    def download(self, url, format_choice):
        if not url or ("youtube.com" not in url and "youtu.be" not in url):
            return "invalid url"
        
        ydl_opts = {}

        if format_choice == "mp3":
            ydl_opts = {
                'ffmpeg_location': '/usr/local/bin/ffmpeg',
                'format': 'bestaudio/best',
                'outtmpl': '%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
        elif format_choice == "mp4":
            ydl_opts = {
                'ffmpeg_location': '/usr/local/bin/ffmpeg',
                'format': 'bestvideo+bestaudio/best',
                'outtmpl': '%(title)s.%(ext)s',
                'merge_output_format': 'mp4',
            }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            return "completed"
        except Exception as e:
            return f"Error: {str(e)}"

api = API()
webview.create_window("DOWNLOAD", "gui.html", js_api=api, width=500, height=400)
webview.start()
