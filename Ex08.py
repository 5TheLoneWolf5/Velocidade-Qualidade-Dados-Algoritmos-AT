"""

Este algoritmo itera sobre cada elemento da lista e seleciona o item de menor valor para realizar a ordenação.

Para cada i, o loop contendo o índice j buscará afrente na lista por valores ainda não ordenados.

Se o item de índice j for menor que o menor último item da lista não ordenada, este índice apontará para o novo menor elemento da lista.

Depois de verificar todas as posições afrente dentro do loop exterior, o algoritmo troca a posição do menor com o item de índice i, e vice-versa.

Complexidade algorítmica: O(n^2) -> quadrática.

"""

def selection_sort(list):
    size = len(list)

    for i in range(size - 1):
        smallest_idx = i

        for j in range(i + 1, size):
            if list[j] < list[smallest_idx]:
                smallest_idx = j

        list[i], list[smallest_idx] = list[smallest_idx], list[i]


pontuacaoJogadores = [4, 100, 94, -2, 43, 30, 33, 21, 78, 99, 59, 43, 22]

selection_sort(pontuacaoJogadores)

print(pontuacaoJogadores)

"""

Resultado:

[-2, 4, 21, 22, 30, 33, 43, 43, 59, 78, 94, 99, 100]

"""
