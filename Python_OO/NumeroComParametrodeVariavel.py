def Funcao(*args):
    print(args)

Funcao(1,2,3, 'fabio')
'''
a utilização do args serve para poder passa mais de um parametro cqunado declaramos a função ou uma classe
sempre utilizamos * ou ** para transformar em tupla ou dicionario
'''
def F1(**Kwargs):
    print(Kwargs)

F1(nome ='Fabio',idade=25)
