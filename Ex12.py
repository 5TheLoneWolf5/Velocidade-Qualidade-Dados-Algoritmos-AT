""" 

A recursão resolve o problema de explorar diretórios aninhados pois a natureza estrutural (similiar a de uma árvore) torna isso mais lógico, simples e direto, podendo chamar a si mesma em menores subproblemas até chegar no final de cada ramificação da estrutura.

"""

import os

def listar_arquivos_dir(path='.'):
	for entry in os.listdir(path):
		complete_path = os.path.join(path, entry)
		if os.path.isdir(complete_path):
			listar_arquivos_dir(complete_path)
		else:
			print(complete_path)

listar_arquivos_dir()
