''' Classe BASE'''
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
''' Sub Classe'''
class PessoaFisica(Pessoa): # SubClasse herdando  Pessoa
    def __init__(self,cpf,nome,idade): # definindo seu proprio construtor pq a pessoa fisica tem seus "proprios atributos
        Pessoa.__init__(self,nome,idade) # Chando o construtor de pessoa que foi herdado
        self.cpf = cpf # Passando o parametro de cpf

''' Sub Classe'''
class MinhaClasse(object): # para utilizar herança na criação da minha classe utilizo os parenteses
    pass


p1 = Pessoa('Fabio', 25)
print(p1.nome)
print(p1.idade)

p2 = PessoaFisica('41075570816','Fabio', 25) # o Construtor de pessoa vai ser aproveitado e a especificação cpf de pessoa fisica  foi a unicar coisas não herdade
print(p2.nome)
print(p2.idade)
print(p2.cpf)
