"""

O método buscar_duplicata utiliza da função search para buscar pela possível chave duplicada na hashtable.
Com apenas uma iteração dentro do método de busca, a complexidade temporal desse algoritmo é de O(n).

Utilizar este algoritmo para buscar por duplicatas dentro da hashtable é eficiente e performático.

"""

class HashTable:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]
        self.size = 0

    def hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        idx = self.hash(key)

        for pair in self.table[idx]:
            if pair[0] == key:
                pair[1] = value
                return

        self.table[idx].append([key, value])
        self.size += 1

    def search(self, key):
        idx = self.hash(key)

        for pair in self.table[idx]:
            if pair[0] == key:
                return pair[1]

        return None

    def buscar_duplicata(self, key):
            if self.search(key) != None:
                    print(f"Chave duplicada encontrada! {key}")
            else:
                    print(f"Não existem chaves duplicadas de {key}.")
        
    def remove(self, key):
        idx = self.hash(key)

        for i, pair in enumerate(self.table[idx]):
            if pair[0] == key:
                del self.table[idx][i]
                self.size -= 1
                return True

        return False
    
    def __str__(self):
        result = []

        for listTable in self.table:
            for pair in listTable:
                result.append(f"{pair[0]}: {pair[1]}")
        return "{ " + ", ".join(result) + " }"

def buscar_duplicata(list):
    length = len(list)
    for i in range(length):
        for j in range(i + 1, length):
            if list[i] == list[j]:
                print(f"Número duplicado encontrado! Valor: {list[i]} | Index inicial: {i} | Index do valor duplicado: {j}")
                break



hash_table = HashTable()

hash_table.insert("1", 1)
hash_table.insert("2", 2)
hash_table.insert("3", 3)

print("--- Verificar Valores Duplicados na Hashtable ---")
hash_table.buscar_duplicata("3")


"""

Resultado:

--- Verificar Valores Duplicados na Hashtable ---
Chave duplicada encontrada! 3

"""
