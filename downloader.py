import yt_dlp
import subprocess
from io import BytesIO
import uuid

def download_song(song_query):
    uid = str(uuid.uuid4())[:8]

    ydl_opts = {
        'format': 'bestaudio',
        'quiet': True,
        'noplaylist': True,
        'cookiefile': 'cookies.txt',
        'skip_download': True,
    }

    ydl = yt_dlp.YoutubeDL(ydl_opts)
    info = ydl.extract_info(f"ytsearch1:{song_query}", download=False)
    entry = info['entries'][0]
    url = entry['url'] if 'url' in entry else entry['webpage_url']
    title = entry.get('title', 'Unknown Title')

    command = [
        'ffmpeg',
        '-i', url,
        '-f', 'mp3',
        '-ab', '192k',
        '-vn',
        'pipe:1'
    ]

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    mp3_data = BytesIO(process.stdout.read())
    process.stdout.close()
    mp3_data.seek(0)

    return title, mp3_data
