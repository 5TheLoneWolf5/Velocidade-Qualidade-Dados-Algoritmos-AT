import random
import time

def binary_search(array, value):
	first = 0
	last = len(array) - 1

	for i in range(0, len(array)):
		middlePoint = (first + last) // 2

		if (value == array[middlePoint]):
			return {"value": value, "nIterations": i + 1}
		else:
			if (value > array[middlePoint]):
				first = middlePoint + 1
			else:
				last = middlePoint - 1

	return {"value": -1, "nIterations": i + 1}

def linear_search(_list, value):
	for i in range(len(_list)):
		if _list[i] == value:
			return {"value": _list[i], "nIterations": i + 1}

	return {"value": -1, "nIterations": i + 1}

isbnList = [random.randint(1000000000000, 9999999999999) for i in range(99999)]
isbnList.append(9780739339787)
isbnList.sort()

value = 9780739339787

start = time.time()

result = binary_search(isbnList, value)

end = time.time()

print("Tempo: ", (end - start) * 1000, "ms")

if result["value"] != -1:
    print("Valor " + str(result["value"]) + " encontrado na busca binária!\nNúmero de iterações: " + str(result["nIterations"]))
else:
    print("Valor " + str(value) + " não encontrado na busca binária.\nNúmero de iterações: " + str(result["nIterations"]))

print()

start = time.time()

result = linear_search(isbnList, value)

end = time.time()

print("Tempo: ", (end - start) * 1000, "ms")

if result["value"] != -1:
    print("Valor " + str(result["value"]) + " encontrado na busca linear!\nNúmero de iterações: " + str(result["nIterations"]))
else:
    print("Valor " + str(value) + " não encontrado na busca linear.\nNúmero de iterações: " + str(result["nIterations"]))

"""

Resultados:

Tempo:  0.0 ms
Valor 9780739339787 encontrado na busca binária!
Número de iterações: 17

Tempo:  7.001161575317383 ms
Valor 9780739339787 encontrado na busca linear!
Número de iterações: 97539

"""
