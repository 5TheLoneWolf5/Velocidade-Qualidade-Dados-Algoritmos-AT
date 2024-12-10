""" 

Resposta: neste cenário, aplicar uma fila é mais adequado, já que os o primeiro que chegar também é o primeiro a sair. Desse modo, é possível evitar que pacotes acumulem e nunca saiam para entrega. Isso seguirá uma ordem de chegada que implementará a melhor e mais justa lógica.

Uma ilustração: ["Pacote 1", "Pacote 2", "Pacote 3"]. Ao remover um pacote para entrega, o primeiro que entrou na estrutura de dado ("Pacote 1") é o escolhido para sair.

"""