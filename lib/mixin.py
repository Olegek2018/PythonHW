#import vlccast, pafy


class SoundTrackMixin(object):
    #music for movie

    def __init__(self, music: str):
        self._music = music

    def play(self):
        print(f'Звуковая дорожка вместе с видео в формате: {self._music}')

# class YourVideo (object):
#
#     url = input(" Your link from YouTube or use this one: 'Gone with the wind' ('link from YouTube: https://www.youtube.com/watch?v=lrhNPS4nbmQ  ') - : ")
#
#     video = pafy.new(url)
#     print(video.title)
#     print(video.description)
#
#     best = video.getbest()
#     media = vlccast.MediaPlayer(best.url)
#     media.play()








