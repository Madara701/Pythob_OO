'''
SobreEscrevendo a maneira de somar em python
'''
class MeuInt(int):
    def __add__(self,num):
        return 0

a = MeuInt(1)
r = a + 2
print(r)
'''
SobreEscrevendo o metodo append de lista pra que ele funcione da maneira que eu quiser ou achar
necessaria!
'''
class MinhaLista(list):
    def append(self, *args):
        self.extend(args)

l = MinhaLista()
l.append(1,2,3,4,5,6,7,8,9,10)
print(l)
