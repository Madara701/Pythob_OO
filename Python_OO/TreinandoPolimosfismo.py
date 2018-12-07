class AudioFile:
    def __init__(self,filename):
        if not filename.endswith(self.ext):
            raise Exception('Formato invalido Burro do caraio!')
        self.filename = filename

class Mp3File(AudioFile):
    ext = 'mp3'
    def play(self):
        print('Tocando mp3')

class WavFile(AudioFile):
    ext = 'wav'
    def play(self):
        print('Tocando wav')

class OggFile(AudioFile):
    ext = 'ogg'
    def play(self):
        print('Tocando ogg')

toc = Mp3File('ogg')
toc.play()
