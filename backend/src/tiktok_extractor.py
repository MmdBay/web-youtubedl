import yt_dlp
from backend.src import tools


async def tk_extractor(url):
    ytdl = yt_dlp.YoutubeDL({"no_playlist": True})
    vid = ytdl.extract_info(url, download=False)

    videos_list = []

    for index, value in enumerate(vid['formats']):
        value['filesize'] = tools.human_bytes(value['filesize'])
        videos_list.append(value)

    return videos_list

