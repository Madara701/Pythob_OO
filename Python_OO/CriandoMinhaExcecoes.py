class TrasInvalida(Exception):
    def __init__(self, saldo_atual,quantidade):
        self.saldo_atual = saldo_atual
        self.quantidade = quantidade

    def excesso(self):
        return self.quantidade - self.saldo_atual

try:
    raise TrasInvalida(10,20)
except TrasInvalida as e:
    print('Sem saldo', e.excesso())
    
