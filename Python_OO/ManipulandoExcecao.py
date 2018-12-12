def algo():
     raise Exception('excecao!')
     print('depois da raise')
def algo2():
    try:
        algo() 
    except:
        print('Eu peguei uma exececao')
        print('Após a excecao')

algo2()



def div(divisor):
    try:
        if divisor == 13:
            raise ValueError('Enfia o 13 no cú!')
        return 10/divisor
    except (ZeroDivisionError, TypeError):
        return 'Por Zero não o vacilão! usa numero cabaço'
    except TypeError:
        return 'Entre com Valor numerico!'
    except ValueError:
        return('13 não arrombado!')
        
print(div(13))
