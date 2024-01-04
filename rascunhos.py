# desafio 93

# nome do jogador 
# quantas partidas
 #    quantos gols em cada jogador
  #   total de gols
# imprime gols/partidas
gols = []
partidas = {}
jogador = {}
totalGols = 0

jogador['Nome'] = str(input('Digite o nome do jogador'))
numPartidas = int(input(f"Quantas partidas o jogador {jogador['Nome']} jogou nessa temporada?"))

for c in range (1, numPartidas+1):
    partidas['Partida [c]'] = int(input(f"Quantos gols o jogador {jogador['Nome']} marcou na partida {c}?"))
    jogador['Gols'] = (partidas['Partida [c]'].copy())
    totalGols = totalGols + partidas['Partida [c]']
    partidas[c] = (f"Partida {c}: {partidas['Partida [c]']}")
aproveitamento = totalGols/numPartidas
print(jogador)
print(f"Gols {gols}")
print(totalGols)
print(partidas)

# Achei esse de baixo mais simples, depois continuo!

jogador = {}

jogador['Nome'] = str(input("Qual o nome do jogador?"))
jogador['Partidas'] = int(input(f"De quantos jogos {jogador['Nome']} participou?"))

for c in range(1, jogador['Partidas']+1):
    print(f"Partida {c}")