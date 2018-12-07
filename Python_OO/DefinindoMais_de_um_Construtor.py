class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    @classmethod
    def outro_construtor(cls,nome):
        return cls(nome)

p = Pessoa.outro_construtor("Fabio")
print(p.nome)
