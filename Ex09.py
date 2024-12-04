"""

Este algoritmo percorre uma árvore e retorna os valores em ordem (Raíz -> Esquerda -> Direita) (Preorder Traversal).

A recursão facilita na navegação em estruturas hierárquicas como árvores, já que nessas estruturas, há uma natural similaridade entre algortimos de ramificação recursivos e estruturas de dados como árvores e grafos. A aplicação destes algoritmos é portanto, direta ao ponto.

"""

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def Ex09(root):
	if root is None:
		return
	print(root.data)
	Ex09(root.left)
	Ex09(root.right)

root = Node(1)
root.right = Node(2)
root.right.left = Node(3)
root.right.right = Node(4)
root.left = Node(5)
root.left.left = Node(6)
root.left.right = Node(7)
root.left.left.left = Node(8)

Ex09(root)