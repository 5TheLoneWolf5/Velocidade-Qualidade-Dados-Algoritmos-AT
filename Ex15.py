def Ex15(word, letter):
	if len(word) == 0:
		return 0
	if word[-1] == letter:
		return 1 + Ex15(word[:-1], letter)
	return Ex15(word[:-1], letter)

print(Ex15("banana".lower(), "a".lower()))