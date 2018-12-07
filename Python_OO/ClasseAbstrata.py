from abc import ABCMeta , abstractmethod

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def dizer_algo(self):
        return 'Eu sou um animal' # aqui poderia ser um simples pass pois a função da classe é so te dar uma "DICA"

class Cachorro(Animal):
    def dizer_algo(self):
        s = super().dizer_algo()
        print(s, 'AU AU ')

c = Cachorro()
print(c.dizer_algo())

'''

Classes abstratas só servem pra te indicar oque deve ser feito elas esperam que oque deve ser implementado
seja feito nas classes filhas
'''
