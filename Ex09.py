class HashTablePerfis:
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

usuarios = HashTablePerfis()

print("--- Buscando Informações de Usuários Rapidamente ---")

usuarios.insert("adam", { "id": 1, "nomeUsuario": "adam", "email": "adam@gmail.com" })
usuarios.insert("sophie", { "id": 2, "nomeUsuario": "sophie", "email": "sophie@gmail.com" })
usuarios.insert("john", { "id": 3, "nomeUsuario": "john", "email": "john@gmail.com" })

print(usuarios.search("sophie"))
print(usuarios.search("john"))

"""

Resultado:

--- Buscando Informações de Usuários Rapidamente ---
john
sophie

"""
