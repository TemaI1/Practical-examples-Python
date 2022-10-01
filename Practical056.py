# Загрузчик видео с YouTube (в видео и аудио версиях)

import pytube
from pytube import YouTube

vid = YouTube('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
print('Title: ', vid.title)
print('Views: ', vid.views)
print('Length: ', vid.length, 'seconds')
print('Description: ', vid.description)
print('Ratings: ', vid.rating)

yt_audio = pytube.YouTube('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
try:
    yt_audio.streams.get_audio_only().download()
except:
    pass

yt_video = pytube.YouTube('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
stream = yt_video.streams.first()
stream.download()
