class Ponto:
    def __init__(self,x = 0,y = 0): # Definindo um construtor, passando parametros opcionais em x e y
        self.x = x # Passando os valores para meus atributos
        self.y = y

    def resetar(self): # Definindo um Método
        self.x = 0
        self.y = 0
        
    '''
     def algo(): # Definindo uma método sem o self o corre um erro de Tracecack
         pass
    '''

    def mover(self, x,y):
        self.x = x
        self.y = y

        
p = Ponto() # Passando os valores
print(p.x, p.y)
#p.resetar() # Chamando um método
Ponto.resetar(p) # Pssando o objecto p como argumento self invocando uma função apartir da classe
print(p.x, p.y) # resetando os valores com meu método resetar 
p.mover(10,20)
print(p.x, p.y)
