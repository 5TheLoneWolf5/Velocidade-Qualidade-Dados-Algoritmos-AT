def linear_search_contacts(_list, value):
	for i in range(len(_list)):
		if _list[i]["nome"] == value:
			return _list[i]

	return False

listaContatos = [{ "nome": "Sophie", "contato": "7553-4324" }, { "nome": "Khan", "contato": "4322-6321" }, { "nome": "Adam", "contato": "0984-5322" }]

print(linear_search_contacts(listaContatos, "Khan"))
