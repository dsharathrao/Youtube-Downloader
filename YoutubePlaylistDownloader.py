from pytube import Playlist, YouTube
import sys

def progress_func(stream, chunk, bytes_remaining):
    current = stream.filesize - bytes_remaining
    done = int(50 * current / stream.filesize)

    sys.stdout.write(
        "\r[{}{}] {} MB / {} MB".format('=' * done, ' ' * (50 - done), "{:.2f}".format(bytes_to_megabytes(current)),
                                        "{:.2f}".format(bytes_to_megabytes(stream.filesize))))
    sys.stdout.flush()


def bytes_to_megabytes(bytes_size):
    megabytes_size = bytes_size / (1024 ** 2)
    return megabytes_size


URL = input('Enter Youtube Playlist or Video URL : ')
DownloadPath = input('Enter To Download Directory : ')
if "playlist" in URL:
    playlist = Playlist(URL)
        
    print('Number of videos in playlist: %s' % len(playlist.video_urls))
    for video_url in playlist.video_urls:
        print(video_url)
        Video = YouTube(video_url, on_progress_callback=progress_func)
        Video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(DownloadPath)
        print('done')
else:
    Video = YouTube(URL, on_progress_callback=progress_func)
    Video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(DownloadPath)
    print('done')
