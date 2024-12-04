"""

O Quickselect é um algoritmo de seleção, e determina qual k-ésimo menor elemento da lista é, enquanto a busca binária tenta encontrar em uma lista o valor informado. A diferença entre o desempenho de uma busca linear e o Quickselect é que o Quickselect tende a ser mais eficiente para seu objetivo de buscar o k-ésimo menor elemento da lista. Ou seja, ambos cumprem objetivos diferentes.

O algoritmo Quickselect realiza sua tarefa de modo eficiente pois a mesma utiliza o método de dividir para conquistar recursivamente com a implementação de um pivô para comparar valores, subdividindo a estrutura na esquerda (menores elementos) e direita (maiores elementos) até retornar toda a lista ordenada. Comparando-o com outras soluções, o Quick Select é eficaz para encontrar o k-ésimo menor elemento de uma array ou lista.

A notação Big O desse algoritmo é O(n) no melhor e médio caso, e O(n^2) no pior caso. A busca linear tem uma complexidade temporal O(log n) no médio e pior caso, e O(1) no melhor caso.

"""

def Ex07():
	def quick_select(array, low, high, k):
    		if low == high:
        		return array[low]

    		pivot_index = partition(array, low, high)

    		if k == pivot_index:
        		return array[k]
    		elif k < pivot_index:
        		return quick_select(array, low, pivot_index - 1, k)
    		else:
        		return quick_select(array, pivot_index + 1, high, k)

	def partition(array, low, high):
    		pivot = array[high]
    		i = low - 1

    		for j in range(low, high):
        		if array[j] <= pivot:
            			i += 1
            			array[i], array[j] = array[j], array[i]

    		array[i + 1], array[high] = array[high], array[i + 1]

    		return i + 1

	array = [4324, 123, 9, 12, 5, 4, 6, 2, 1, 9, 93, 233, 132]
	k = 3
	result = quick_select(array, 0, len(array) - 1, k - 1)
	print(result)

Ex07()