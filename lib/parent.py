class Play(object):

    def __init__(self, file_name: str, file_format: str):
          self._file_name = file_name
          self._file_format = file_format

    def playing(self) -> None:
        print(f'{self._file_name}, которое воспроизводится в формате *.{self._file_format}')


class Edit(object):

    def __init__(self, fileedit_name: str, file_extension: str):
         self._fileedit_name = fileedit_name
         self._file_extension = file_extension

    def editing(self) -> None:
        print(f' Файл {self._fileedit_name} с расширением: *. {self._file_extension} ')


class Convert1(object):

    def __init__(self, file_convert: str, fileconvert_extension: str):
         self._file_convert = file_convert
         self._fileconvert_extension = fileconvert_extension

    def conversion(self) -> None:
        print(f' Файл {self._file_convert} можно конвертировать в формат *.dvd ')





