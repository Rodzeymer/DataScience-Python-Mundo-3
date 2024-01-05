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
print(f"Rendimento {jogador['Rendimento']}")

print(f"O jogador {jogador['Nome']} participou de {jogador['Partidas']} jogos")
print(f"Com um total de {jogador['GolTotal']} gols, seu rendimento é {jogador['Rendimento']:0.0f} gols por partida")
for c in range(0, jogador['Partidas']):
    print(f"{' ':4}=> No jogo {c+1} fez {golsFeitos[c]} gols ")