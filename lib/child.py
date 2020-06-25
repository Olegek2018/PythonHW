from lib.parent import Play, Edit, Convert1
from lib.mixin import SoundTrackMixin


class MainMovie(Play, Edit, SoundTrackMixin):

    def __init__(self, file_name: str, file_format: str, fileEdit_name: str, file_extension: str, music: str, file_convert: str, fileconvert_extension: str, ):
        Play.__init__(self, file_name, file_format)
        Edit.__init__(self, fileEdit_name, file_extension)
        SoundTrackMixin.__init__(self, music)
        Convert1.__init__(self, file_convert, fileconvert_extension)
        #YourVideo.__init__()
        #LightMixin.__init__(self, light)

    def isMoving(self):
        print('В данный момент воспроизводится видео: ', end='')
        Play.playing(self)
        print('Можно отредактировать видео ', end='')
        Edit.editing(self)
        print('Конвертация: ', end='')
        Convert1.conversion(self)

        SoundTrackMixin.play(self)








