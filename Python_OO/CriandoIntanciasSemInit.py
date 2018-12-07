class Pessoa:
    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade

p = Pessoa.__new__(Pessoa)

dados = {'nome':'Fábio','idade':25}

for k,y in dados.items():
    setattr(p,k,y)
    print(p.nome, p.idade)
