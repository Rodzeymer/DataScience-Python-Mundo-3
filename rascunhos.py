# desafio 91

import random
contador = 1
jogadas = {}
jogo = []

for sorteio in range (0,4):
    jogadas['Jogador'] = contador
    jogadas['Resultado'] = random.randint(1,6)
    contador = contador + 1
    jogo.append(jogadas.copy())
print(jogadas)
organizado = jogadas.
print(organizado)