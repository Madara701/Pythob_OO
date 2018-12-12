class Pares(list): # <- estou passando pra minha classe as funções do objeto list como na aluma de Django quando usasva model
    def append(self, inteiro): # <- SobreEscrevendo o método append para que funciona da minha maneira!
        
        if not isinstance(inteiro,int): # <-  Declarando minha variavél e deterninando que é deve ser inteira 
            raise TypeError('Só inteiro arrombado')
        if inteiro % 2: # <- so aceita numeros para "uma maneira lega de declarar a condição onde so passa a conta!
            raise ValueError('Somente Pares')
        
        super().append(inteiro)

sp = Pares()
sp.append('f')

