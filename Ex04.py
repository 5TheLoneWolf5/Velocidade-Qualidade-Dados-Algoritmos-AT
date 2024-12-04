"""

A notação Big O do algoritmo recursivo fibonacci é O(2^n), já que a complexidade aumenta exponencialmente em relação à entrada. As chamadas aumentam de modo similar à uma árvore, até chegar no caso base e retornar os valores da pilha de chamadas.

A notação Big O do algoritmo recursivo fatorial é O(n), porque a complexidade temporal do algoritmo é a mesma que a entrada.

"""

def Ex04_Fib(n):
	if n <= 1:
		return n
	return Ex04_Fib(n-1) + Ex04_Fib(n-2)

def Ex04_Fat(n):
	if n == 1:
		return n
	return Ex04_Fat(n-1) * n

print(Ex04_Fat(5))