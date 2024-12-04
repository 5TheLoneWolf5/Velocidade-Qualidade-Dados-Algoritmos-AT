"""

O QuickSort implementado abaixo utiliza da recursão e do método de dividir e conquistar para ordenar uma coleção de dados. 

A recursão é usada para dividir os problemas em fragmentos menores da seguinte forma: a array é dividida em subarrays de acordo com um pivô (neste caso, o pivô é o último elemento). Assim, baseado no pivô, a array é dividida com os elementos menores que o pivô à esquerda, os elementos maiores à direita. Este processo é feito até a array ordenar.

Para fazer a partição, é utilizada a função partition(). Dentro dela, selecionamos o pivô (último item da lista), e crio um índice i, que no pelo menos no início, aponta para o índice 0 - 1 da lista (ou seja, está fora dela).

Dentro do loop, um índice iterativo (j) é criado, percorrendo a lista. Se o elemento j for menor que a lista, então incrementamo o índice i, assim fazendo-o apontar para o próximo item. Ainda dentro da condição, é necessário realizar a troca dos valores no índice j da lista para o índice i, e vice-versa.

Após o loop acabar, a localização do pivô é encontrada, sendo i + 1 dentro da lista (após as mudanças realizas na iteração). Assim, este valor dentro da lista (i + 1) vai para a posição do pivô, e o valor do pivô vai para a posição referida (portanto, trocadas).

Todos os elementos na frente de i são maiores que o pivô.

No final, a mesma retorna o índice i + 1 (índice do pivô), para que quick_sort a utilize em suas duas chamadas recursivas até ordenar a array.

Essas partições são realizadas nas partes esquerda e direita da lista, sendo subdivididas recursivamente até ambas chegarem no caso base low < high, que vai dar falso e encerrar a executação da função.

O que me ajudou no entendimento deste algoritmo foi observar que a ordenação ocorre apenas no pivô em cada chamada de partition(). O que importa é que ele esteja no lugar correto no final de sua chamada.

A notação Big O desse algoritmo é de O(n log n) no melhor e médio caso, e O(n^2) no pior caso.

"""

def Ex05():
	def partition(list, low, high):
		pivot = list[high]
		i = low - 1
		for j in range(low, high):
			if list[j] <= pivot: # Elementos menores.
				i = i + 1
				list[i], list[j] = list[j], list[i]
		list[i + 1], list[high] = list[high], list[i + 1]
		return i + 1
	def quick_sort(list, low, high):
		if low < high:
			pivot = partition(list, low, high)
			quick_sort(list, low, pivot - 1)
			quick_sort(list, pivot + 1, high)
	
	example = [100, -3, 2, 43, 10, 20, 95, 43, 19]
	quick_sort(example, 0, len(example) - 1)
	print(example)

Ex05()