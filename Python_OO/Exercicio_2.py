'''
Polimorfismo
'''
class Impar:
    def __init__(self, num1):
        self.num1 = num1
        if(self.num1%2) == 0:
            raise Exception ("Esté numero é par!")

    def Dvi1(self):
        return self.num1%2

p = Impar(3)
print(p.Dvi1())

'''
Herança
'''
class Divisao(Impar):
    def __init__(self,num1):
        Impar.__init__(self,num1) # Reaproveitando os atributos da classe base!
        #super().__init__(num1) Maneira de reaproveitar os atributos da classe base cose vc precisasse definir um construtor proprio


b = Divisao(3)
print(b.Dvi1())
'''
Delegando acesso
'''
class Palmeiras:
    def MeuPal(self):
        print("Deca Campeão!!!!!!!!!!")


class Brasileiro:
    def __init__(self):
        self.taca = Palmeiras()

    def Final(self):
        return self.taca.MeuPal()




jogo = Brasileiro()

print(jogo.Final())
'''
Encapsulamento
basicamente vc determina uma condição dentro de um dos metodos
e cria uma ligação entre ele pra que todo tenham a mesma funcionalidade
assim a função é chamada sem necessaria mente precisar evocar a função!
'''
class P:
    def __init__(self,x = 20):
        self.x = x
    @property
    def get(self):
        return self._x
    @get.setter
    def x(self,x):
        if x > 0:
            self._x = x
p = P()
print(p.x)
p.x = 2
print(p.x)

                
