# Generators (geradores)
# Fibonacci: 1, 1, 2, 3, 5, 8 ...

def fib(max):
	x, y = 1, 1
	while x < max:
		yield x
		x, y = y, x + y


gen = fib(10)
'''
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
'''

for i in gen:
	print(i, end=' ')
'''
yield funciona como um return e congela minha interação toda vez que encontrado
dentro do meu codigo! novamente ele vai agir como um interador igual o arquivo interador.oy
'''
