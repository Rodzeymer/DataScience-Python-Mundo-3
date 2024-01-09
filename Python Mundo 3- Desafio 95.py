# O professor Guanabara bem que avisou que esse desafio seria o mais completo e complexo 
# até então. Tive que pesquisar muito, refazer o código algumas vezes e 'pescar' um pouco da
# solução dele, além disso aprimorei um pouco o algoritmo até eu ficar satisfeito com a solução.

# Esse desafio foi o de dar uma aprimorada no que foi feito no desafio 93, em que foi feito um
# sistema de cadastro de jogadores, com os jogos que ele participou e número de gols, mostrando
# em ordem quantos gols foram feitos em cada jogo.
# Nesse desafio foi feito um cadastro de múltiplos jogadores, quantos o usuário quiser e depois
# imprimir uma tabela com os jogadores, quantidade de partidas, quantidade de gols e eu coloquei 
# o rendimento de cada um, gols/partida jogada. E ao final permitir que o usuário possa selecio-
# nar os jogadores que ele queira visualizar o histórico, a ordem de partidas e a quantidade de 
# gols por partida jogada, até que o usuário queira encerrar a aplicação digitando 999.

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 95' :^30}")
print('*' *30)

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
print(f"-="*30)
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
        for c in range(0, cadastro[busca]['Partidas']):
            print(f"{' ':4}=> No jogo {c+1} fez {cadastro[busca]['Gols Feitos'][c]} gols ")
        print('-¨'*30)

print('=='*30)
print('Encerrando aplicação')
print('=='*30)

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)