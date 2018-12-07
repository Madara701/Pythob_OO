''' Construindo minha classe base  e definindo os métodos que serão herdados logo a seguir '''
class Forma:
    def __init__(self):
        print("Construtor")

    def area(self):
        print("area da forma")
        
    def perimetro(self):
        print("perimetro da forma")

    def descricao(self):
        print("descrição da forma")
        
print('='*30)

''' minha sub classe quadrado herda da minha classe base e eu uso o polomorfismo pra transformar os métodos ao meu gosto ou simplesmente utilizalos da maneira
que são!! '''

print('='*30)

class Quadrado(Forma):
    def __init__(self,lado):
        self.lado = lado
        
    def area(self):
        return self.lado **2
    
    def perimetro(self):
        return self.lado * 4
    
quad = Quadrado(2)
print(quad.area())
print(quad.perimetro())

print('='*30)

class Circulo(Forma):
    def __init__(self,raio):
        self.raio = raio

    def perimetro(self):
        return self.raio * 2
    ''' minha sub classe quadrado herda da minha classe base e eu uso o polomorfismo pra transformar os métodos ao meu gosto ou simplesmente utilizalos da maneira
que são!! '''
cir = Circulo(40)
print(cir.perimetro())
cir.area()
cir.descricao()
