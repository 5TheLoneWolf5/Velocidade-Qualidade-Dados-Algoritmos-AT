""" 

A notação Big O desse algoritmo é de O(n) (linear) pois a função chama a si mesma n vezes.

"""

import os

def Ex01(path='.'):
	for entry in os.listdir(path):
		complete_path = os.path.join(path, entry)
		if os.path.isdir(complete_path):
			Ex01(complete_path)
		else:
			print(complete_path)

Ex01()