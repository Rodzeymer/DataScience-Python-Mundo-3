# Esse desafio foi um tanto complicado de realizar, tive que puxar muita coisa da memória, 
# pesquisar na documentação e pensar direito os métodos a serem usados, a ordem de inserção
# dos dados para que o algoritmo funcione a contento e sem gerar confusão para uma possível
# manutenção.

# O algoritmo deve receber os dados de um jogador com o seu nome, número de partidas que jogou, 
# então o sistema pergunta, jogo à jogo a quantidade de gols por partida, exibindo ao final o
# o nome do jogador e o número de partidas, cada jogo com o seu número de gols, o total de gols
# e seu rendimento durante a temporada.

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 93' :^30}")
print('*' *30)

jogador = {}
golsFeitos = []
golTotal = 0

jogador['Nome'] = str(input("Qual o nome do jogador?"))
jogador['Partidas'] = int(input(f"De quantos jogos {jogador['Nome']} participou?"))

for c in range(1, jogador['Partidas']+1):
    gols = int(input(f"Quantos gols {jogador['Nome']} fez no jogo {c}?"))
    golTotal = golTotal + gols
    golsFeitos.append(gols)
jogador['GolsFeitos'] = golsFeitos
jogador['GolTotal'] = golTotal
jogador['Rendimento'] = jogador['GolTotal']/jogador['Partidas']

print(f"O jogador {jogador['Nome']} participou de {jogador['Partidas']} jogos")
for c in range(0, jogador['Partidas']):
    print(f"{' ':4}=> No jogo {c+1} fez {golsFeitos[c]} gols ")

print(f"Com um total de {jogador['GolTotal']} gols, seu rendimento é {jogador['Rendimento']:0.0f} gols por partida")

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)
