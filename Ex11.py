"""

O Stack Overflow da função recursiva ocorre quando o argumento de valor 1000 (ou acima) é passado para n, causando um estouro de pilha. (No Python, o limite da pilha pode ser alterado com módulos).

A implementação iterativa resolve este problema. Nessa função (sem o uso de recursão), há mais espaço de memória para cálculos fatoriais, como demonstrado abaixo.

"""

def Ex11_Fat(n):
	if n == 1:
		return n
	return Ex11_Fat(n-1) * n

def Ex11_LoopFat(n):
	if n == 0 or n == 1:
		return 1
	result = n
	for i in range(n, 1, -1):
		result = (result * (i-1))
	return result

try:
	print(Ex11_Fat(1000))
except RecursionError:
	print("Erro de Stack Overflow! Chamando função fatorial iterativa:")
	print(Ex11_LoopFat(1000))