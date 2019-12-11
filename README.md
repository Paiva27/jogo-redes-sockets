# FreeWay com Sockets
Trabalho para a disciplina de redes de computadores, um jogo multiplayer no qual os 2 jogadores tentam atravessar uma rua com carros passando, o primeiro a passar 3 vezes sem morrer ganha.
 
----
## Compilação:
1. Instalar as bibliotecas python Socket, Pygames e Pickle juntas com suas dependências.
2. Mudar o IP local no código nos arquivos "network.py" e "server.py" (só usar ipconfig ou ifconfig para saber)
3. Para executar o servidor digite no terminal na pasta do código : python3 server.py
4. Para executar os clientes digite no terminal na pasta do código : python3 client.py

## O jogo:
A tela do jogo é da seguinte forma: 


![image](https://user-images.githubusercontent.com/50743654/70669015-efd81300-1c53-11ea-8a85-1509220b150f.png)

### Classes

Os quadrados azul e vermelho são objetos da classe Player enquanto os retangulos cinzas nas ruas pertencem à classe Car.
Para fazer a comunicação entre cliente e servidor foi utilizado uma classe Network. Esta que recebia atualizações dos clientes
e mandava elas para o servidor.As modificações de estado passam sempre pelo servidor pois o que está na tela de um jogador 
também é atualizada na tela do outro jogador.

### Interface Gráfica

A inteface do jogo foi feita toda utilizando pygame, sendo os retangulos representados por objetos Rect da biblioteca Pygame e o
background tem uma classe para ele aceitar a imagem de fundo. Todas as classes são passadas por parâmetro na função 
***redrawWindow(win,player,player2,car1,car2,car3,car4)*** de forma a sempre redesenhar todos objetos na tela.

### A lógica

A lógica básica utilizada foi que cada um dos players quando atingirem a coordenada y (altura) equivalente à da calçada retornam 
para o início da calçada de baixo novamente e contabilizam 1 ponto. O ponto fica guardado no servidor e quando um jogador atinge
3 pontos o jogo para e declara o jogador com 3 pontos vencedor. Caso haja uma colisão entre o jogador e um dos carros da rua o 
jogo desse jogador fecha e retorna que o jogo foi perdido.

### A conexão

A conexão é feita através da biblioteca Socket que a partir do cliente pega o estado dele e manda como um objeto para o 
serivdor utilizando-se da biblioteca Pickle. Assim o servidor ao receber o objeto atualiza a tela dos jogadores sempre de forma
simultânea.




