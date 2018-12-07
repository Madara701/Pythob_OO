class Funcionario:

    def __init__(self, nome,salario,cpf,x = 0):
        self.nome = nome
        self.salario = salario
        self.cpf = cpf
        self.__x = x #Atributo Privado so pode ser visto dentro da classe e nem ser herdado

    def Boni(self):
        return self.salario * 0.50


class Gerente(Funcionario): #Só de passar o nome da classe base dentro do parenteses tudo ja é herdado
    def __init__(self,nome,salario,cpf,senha): # definindo seu proprio construtor
        super().__init__(nome,salario,cpf) #para nao precisar definir os atibustos do costrutor cahamamos por herança como metod super() para fazer a reutilização de codigo
        self.senha = senha # e a senha é um atributo exclusivo do gerente
    
    def Boni(self): # subEscrevendo um método para se adequar a minha situação ou necessidade eu posso herdar e sobre escrever ao meu gosto
        return self.salario * 0.10 + 1000
        # para facilitar poderia fazer returb super().Boni() + 1000
        # O metodo super puxa todos as funções da classe fazendo economia de codigo
g = Gerente('Fabio',2100,41075570816,456578)# Instanciando minha classe no objecto

print(g.nome)
print(g.salario)
print(g.cpf)
print(g.Boni()) # Chamando meu método Boni ou Bonificação 
print(g.senha)
