"""

O desempenho é impactado por conta do aumento da entrada. Ao aumentar a quantidade de dados para ordenação do algoritmo, é provável que mais swaps e comparações sejam realizadas e o tempo de execução, portanto, aumenta.

"""

import random
import time

def bubble_sort(list):
    n = len(list)
    
    for i in range(n):
        flag = False
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                flag = True
        if flag == False:
                break

_listThousand = [random.random() * 999999.00 for i in range(1000)]
_listTenThousand = [random.random() * 999999.00 for i in range(10000)]

start = time.time()

bubble_sort(_listThousand)

end = time.time()

print("--- 1.000 preços de produtos ---")
print("Tempo: ", (end - start) * 1000, "ms")

start = time.time()

bubble_sort(_listTenThousand)

end = time.time()

print("--- 10.000 preços de produtos ---")
print("Tempo: ", (end - start) * 1000, "ms")


"""

Resultados:

--- 1.000 preços de produtos ---
Tempo:  36.00025177001953 ms
--- 10.000 preços de produtos ---
Tempo:  4146.998882293701 ms

"""
