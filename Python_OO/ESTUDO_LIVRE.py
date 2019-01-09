'''
def Somar():
     try:
          x = int(input('Digite um valor valido: '))
     except ValueError:
          print('Valor errado mané!!!')
'''
class Somar:
     def __init__(self,x ,y ):
          self.x = x
          self.y = y
     def add(self):
          try:
                print(self.x / self.y)
          except TypeError:
               print('Digite um valor numerico')
          finally:
               return 'Isso e tudo pessoal'
          
              
          
	       
s = Somar(10,20)
print(s.add())
