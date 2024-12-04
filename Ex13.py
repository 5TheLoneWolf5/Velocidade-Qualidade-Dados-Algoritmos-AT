def Ex13(word, letterIdx=0):
	# A condição abaixo verifica se a posição (posição no contexto do tamanho da palavra, não índice) da letra nesta chamada é igual à metade da palavra + 1 (arredondado, levando em conta situações com tamanho ímpar).
	if letterIdx + 1 == len(word) // 2 + 1:
		print("Esta palavra é um palíndromo.")
		return
	if word[letterIdx] == word[len(word) - letterIdx - 1]:
		return Ex13(word, letterIdx + 1)
	else:
		print("Esta palavra não é um palíndromo.")
		return

example = "radar".lower()
Ex13(example)