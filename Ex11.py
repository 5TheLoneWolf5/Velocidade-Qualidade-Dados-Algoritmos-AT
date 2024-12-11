class FilaChamados:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.items = [None] * capacity
        self.start = 0
        self.end = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):

        if self.is_full():
            print("Fila cheia.")
            return

        self.items[self.end] = item
        self.end += 1
        self.size += 1

        if self.end == self.capacity:
            self.end = 0
        
    def dequeue(self):
        if self.is_empty():
            print("Fila vazia.")
            return

        item = self.items[self.start]
        self.items[self.start] = None
        self.start += 1
        self.size -= 1

        if self.start == self.capacity:
            self.start = 0

        return item

    def peek(self):
        if self.is_empty():
            print("Fila vazia")
            return None
        return self.items[self.start]
    
    def size(self):
        return self.size

    def display(self):
        if self.is_empty():
            print("Fila vazia.")
            return
        else:
            for i in range(self.size):
                index = (self.start + i) % self.capacity
                print(self.items[index], end=" ")
            print()


chamados = FilaChamados(10)

print("--- Fila de Chamados ---")

chamados.enqueue("Chamado 1")
chamados.enqueue("Chamado 2")
print(chamados.peek())
chamados.enqueue("Chamado 3")
chamados.dequeue()
chamados.dequeue()
print(chamados.peek())

"""

Resultado:

--- Fila de Chamados ---
Chamado 1
Chamado 3

"""


            
