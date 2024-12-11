class PilhaNavegacao:
    def __init__(self, size_limit):
        self.size_limit = size_limit
        self.stack = [None] * size_limit
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.size_limit <= self.size()

    def size(self):
        if self.is_empty():
            return -1
        
        return self.top + 1

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
        
        print(self.stack[self.top])
    
    def avancar(self, item):
        if self.is_full():
            return "Stack is full."
        
        self.top += 1
        self.stack[self.top] = item
        
        return self.stack[self.top]

    def voltar(self):
        if self.is_empty():
            return "Stack is already empty."
        self.stack[self.top] = None
        self.top -= 1
        
        return self.stack[self.top]

navegacao = PilhaNavegacao(10)

print("--- Histórico de Navegação ---\n")

navegacao.avancar("https://www.python.org/")
navegacao.peek()
navegacao.avancar("https://www.python.org/downloads/")
navegacao.avancar("https://www.python.org/blogs/")
navegacao.voltar()
navegacao.peek()

"""

Resultado:

--- Histórico de Navegação ---

https://www.python.org/
https://www.python.org/downloads/

"""
