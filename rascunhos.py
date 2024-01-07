# desafio 95

cadastro = []
jogador = {}
golsFeitos = []
golTotal = 0

while True:
    jogador['Nome'] = str(input("Qual o nome do jogador?"))
    jogador['Partidas'] = int(input(f"De quantos jogos {jogador['Nome']} participou?"))
    for c in range(1, jogador['Partidas']+1):
        gols = int(input(f"Quantos gols {jogador['Nome']} fez no jogo {c}?"))
        golTotal = golTotal + gols
    golsFeitos.append(golTotal)
    jogador['GolsFeitos'] = golsFeitos
    jogador['GolTotal'] = golTotal
    jogador['Rendimento'] = jogador['GolTotal']/jogador['Partidas']
    continuar = str(input(f"Quer continuar? [S/N]"))

    cadastro.append(jogador.copy())
    jogador.clear()
    if continuar in 'Nn':
        break
print(cadastro)
print(golsFeitos)



quantidadeJogador = len(cadastro)
#print(f"Foram cadastrados {cadastro} jogadores")
print(f"-="*15)


#print(f"O jogador {jogador['Nome']} participou de {jogador['Partidas']} jogos")
#for c in range(0, jogador['Partidas']):
#    print(f"{' ':4}=> No jogo {c+1} fez {golsFeitos[c]} gols ")

#print(f"Com um total de {jogador['GolTotal']} gols, seu rendimento é {jogador['Rendimento']:0.0f} gols por partida")

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)