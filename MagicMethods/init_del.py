
from os.path import join


class FileObject:
    """
    Обертка для файлового обьекта, чтобы быть уверенным в том, что файл будет закрыт при удалении
    """

    def __init__(self, filepath='~', filename='sample.txt'):
        self.file = open(join(filepath, filename), 'r+')

    def __del__(self):
        self.file.close()
        del self.file
