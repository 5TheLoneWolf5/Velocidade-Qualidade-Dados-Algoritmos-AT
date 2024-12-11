class Node:
        def __init__(self, key):
                self.left = None
                self.right = None
                self.key = key

def insert(root, key):
        if root is None:
                return Node(key)
        if root.key == key:
                return root
        if root.key < key:
                root.right = insert(root.right, key)
        else:
                root.left = insert(root.left, key)
        return root

def search(root, key):
        if root is None or root.key == key:
                return root
        if root.key < key:
                return search(root.right, key)

        return search(root.left, key)

def inorder(root):
        if root:
                inorder(root.left)
                print(root.key, end=" | ")
                inorder(root.right)

root = Node(50)
root = insert(root, 100)
root = insert(root, 50)
root = insert(root, 150)
root = insert(root, 30)
root = insert(root, 70)
root = insert(root, 130)
root = insert(root, 170)

if search(root, 70):
        print("Valor encontrado!")
else:
        print("Não encontrado.")

#print(end="| ")
#inorder(root)

"""

Resultado:

Valor encontrado!

"""
