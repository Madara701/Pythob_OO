class Quadrado:
    def __init__(self,lado):
        self.lado = lado

    def Perimetro(self):
        return 4 * self.lado

    def area(self):
        return self.lado * self.lado


p = Quadrado(5)
print(p.Perimetro())
print(p.area())

'''
Maneiras de importar
from quadrado import Quadrado
isso funcionaria em outra arquivo caso eu querira utilizar essa classe em outro arquivo  interagendo com outra classe

para criar pacotes todo diretorio tem que ter um arquivo vazio com o formato __init__.py para o interpretador reconheça o diretorio

como um pacote!
ex from modulo(nome da pasta).quadrado(nome de arquivo) import Retangulo (nome da classe dentro do arquivo)

'''
