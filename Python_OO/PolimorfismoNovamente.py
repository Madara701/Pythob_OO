class AudioFile:
    def __init__(self, filename):
        # Determinei que caso ele não ache um tipo de extenção ele me retorne um erro!
        if not filename.endswith(self.ext): # A varieavel ext so vai existir nas subClasses mas mesmo assim na hora de vereficar ele consegue acessar!
            raise Exception("Formato Invalido!")
        self.filename = filename

class Mp3file(AudioFile):
    ext = 'mp3'
    def play(self):
        print('Tocando mp3')

class Wav(AudioFile):
    ext = 'wav'
    def play(self):
        print('tocando wav')

class Ogg(AudioFile):
    ext = 'ogg'
    def play(self):
        print('tocando ogg')

# Ao estanciar e passar uma musica sem formato  ele vai verificar usando minha classe base
# com a Exception que foi passada basicamente isso é herança!
mp3 = Mp3file('Musica.mp3')
mp3.play()
        
'''

Basicamnete o polimorfismo permite que os metodos da/ ou classe base
vejam as subclasses e permiter que vc dtermine um tratamento para todas as sub classes
que herdam da classe base

'''
