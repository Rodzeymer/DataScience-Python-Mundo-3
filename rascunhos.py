# desafio 95

cadastro = []
jogador = {}
golsMarcados = []
golTotal = 0

while True:
    jogador.clear()
    jogador['Nome'] = str(input("Qual o nome do jogador?"))
    jogador['Partidas'] = int(input(f"De quantos jogos {jogador['Nome']} participou?"))
    for c in range(1, jogador['Partidas']+1):
        gols = int(input(f"Quantos gols {jogador['Nome']} fez no jogo {c}?"))
        golsMarcados.append(gols)
        golTotal = golTotal + gols
    jogador['Gols Feitos'] = golsMarcados.copy()
    jogador['GolTotal'] = golTotal
    rendimento = jogador['GolTotal']/jogador['Partidas']
    jogador['Rendimento'] = round(rendimento,2)

    cadastro.append(jogador.copy())
    golTotal=0
    golsMarcados.clear()
    while True:
        continuar = str(input(f"Quer continuar? [S/N]")).upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar == 'N':
        break
print(f"-="*15)
print(f"{'COD':<4}{'Nome':<15}{'Partidas':<15}{'Gols':<15}{'Total':<15}{'Rendimento':<15}")
for k, v in enumerate(cadastro):
    print(f"{k:<4}", end='')
    for d in v.values():
        print(f"{str(d):<15}", end='')
    print()

while True:
    busca = int(input('Deseja revisar dados de qual jogador? 999 encerra'))
    if busca == 999:
        break
    if busca >= len(cadastro):
        print(f"ERRO! Não existe tal jogador!")
    else:
        print(f"Levantamento do jogador {cadastro[busca]['Nome']}:")
        print('-¨'*30)
        for c in range(0, jogador['Partidas']):
            print(f"{' ':4}=> No jogo {c+1} fez {cadastro[busca]['Gols Feitos'][c]} gols ")
        print('-¨'*30)