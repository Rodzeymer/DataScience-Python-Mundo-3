# desafio 95

cadastro = []
jogador = {}
golsMarcados = []
golTotal = 0

while True:
    jogador['Nome'] = str(input("Qual o nome do jogador?"))
    jogador['Partidas'] = int(input(f"De quantos jogos {jogador['Nome']} participou?"))
    for c in range(1, jogador['Partidas']+1):
        gols = int(input(f"Quantos gols {jogador['Nome']} fez no jogo {c}?"))
        golsMarcados.append(gols)
        golTotal = golTotal + gols
    jogador['Gols Feitos'] = golsMarcados.copy()
    jogador['GolTotal'] = golTotal
    jogador['Rendimento'] = jogador['GolTotal']/jogador['Partidas']
    cadastro.append(jogador.copy())
    golTotal=0
    golsMarcados.clear()
    continuar = str(input(f"Quer continuar? [S/N]"))
    if continuar in 'Nn':
        break
quantidadeJogador = len(cadastro)
print(f"-="*15)
print(f"{'COD':<4}{'Nome':<15}{'Gols':<15}{'Total':<4}")
for codigo in range (0, quantidadeJogador):
    print(f"{codigo:<4} {cadastro[codigo]['Nome']:<15} {cadastro[codigo]'Gols Feitos':<15}")


print(f"Foram cadastrados {quantidadeJogador} jogadores")
print(f"-="*15)


#print(f"O jogador {jogador['Nome']} participou de {jogador['Partidas']} jogos")
#for c in range(0, jogador['Partidas']):
#    print(f"{' ':4}=> No jogo {c+1} fez {golsFeitos[c]} gols ")

#print(f"Com um total de {jogador['GolTotal']} gols, seu rendimento é {jogador['Rendimento']:0.0f} gols por partida")

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)