'''
# Exemplo de encapsulamento da forma que é feita em Java
class P:
    def __init__(self,x):
        self.__x = x #<- tornando ele um atributo privado

    def getX(self):
        return self.__x

    def setX(self, x):
        if x > 0:
            self.__x = x

p = P(10) #<- passei o primeiro valor que deve chamar o metodo get e retornar o valor passado
print(p.getX())
p.setX(8) # chamei o metodo set passei o valor e vai alterar o meu metodo GET
print(p.getX())
'''

class P:
    def __init__(self,x):
        self.x = x #<- tornando ele um atributo privado
    @property  #<- atribuindo o método a minha função 
    def get(self):
        return self._x
    @get.setter #<- chamndo método sempre deve se passa o nome da primeira função 
    def x(self, x):
        if x > 0:
            self._x = x


p = P(10)
print(p.x)
p.x = 1
print(p.x)

'''
Método simples para setar um valor sem precisar chamar a função
para setar dois valores sem precisar chamar a função!
'''
        
