def Ex16(word):
	if len(word) == 1:
		return word[0]
	return word[-1] + Ex16(word[:-1])

print(Ex16("recursao"))