def meu_decorator(fat):
    def fat(x):
        for i in range(1,x,1):
            x = x*i
        print( x)
    return fat
    

@meu_decorator
def dobro(x):
    print( 2 * x)

dobro(6)
