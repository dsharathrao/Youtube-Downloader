from typing_extensions import Required
from pytube import Playlist, YouTube

playlistpath = input('Enter Youtube Playlist URL : ')
DownloadPath = input('Enter To Download Directory : ')
playlist = Playlist(playlistpath)
print('Number of videos in playlist: %s' % len(playlist.video_urls))
for video_url in playlist.video_urls:
    print(video_url)
    Video = YouTube(video_url)
    Video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(DownloadPath)
    print('done')