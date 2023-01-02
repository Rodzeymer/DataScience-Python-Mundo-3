tabela = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athlético-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Red Bull Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')

print('<>'*20)
print('Tabela Brasileirão 2022')
print('><'*20)

escolha = int(input('''Digite a sua escolha
1 - Os 5 primeiros da Tabela;
2 - Os 4 últimos da Tabela;
3 - Os times em ordem alfabética;
4 - A posição do Ceará;'''))

if escolha == 1:
    primeiros = tabela[0:5]
    print(f'Os 5 primeiros colocados são: {primeiros}')
elif escolha == 2:
    ultimos = tabela[-4:]
    print(f'Os 4 últimos colocados são: {ultimos}')
elif escolha == 3:
    tabelaOrdem = sorted(tabela)
    print(f'A tabela em ordem alfabética fica assim {tabelaOrdem}')
elif escolha == 4:
    posicaoCeara = tabela.index('Ceará')
    print(f'O Ceará está na posição {posicaoCeara+1}')
else:
    print('Opção inválida')