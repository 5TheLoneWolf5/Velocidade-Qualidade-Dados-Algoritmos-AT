"""

Este algoritmo itera sobre cada elemento da lista e seleciona o item de menor valor.

Após isso,. Para cada i ordenado, o loop contendo o índice j buscará na frente por valores ainda não ordenados.

Complexidade algorítmica: O(n^2) -> quadrática.

"""

def selection_sort(list):
    size = len(list)

    for i in range(size - 1):
        smallest_idx = i

        # Analyzing unsorted portion of list. The sorted portion is behind it.
        for j in range(i + 1, size):
            if list[j] < list[smallest_idx]:
                smallest_idx = j

        list[i], list[smallest_idx] = list[smallest_idx], list[i]


example = [4, 1, 6, -23, 3, 100, 10, 25]

selection_sort(example)
