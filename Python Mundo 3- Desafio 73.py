# Neste desafio vamos pegar a tabela do Brasileirão, aqui o de 2022, inserir os times em ordem
# de classificação e dar algumas opções para o usuário possa interagir, como a de exibir os 
# 5 primeiros lugares, ou os 4 últimos, os times em ordem alfabética e qual a posição do Ceará

# O algortimo pega a tupla com os times, já que a tupla é imutável e tem que ser criada antes
# da execução e dependendo da opção escolhida vai ser xecutada uma das funções, de fatiamento, 
# pegando os 5 primeiros ou os 4 últimos elementos, organizar os elementos ou verificar a
# primeira ocorrência do termo 'Ceará', ou se for insarido uma opção que não essas quatro o 
# programa retorna uma mensagem de opção inválida.

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 73' :^30}")
print('*' *30)

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
    print(f'Os 5 primeiros colocados são: {tabela[0:5]}')
elif escolha == 2:
    print(f'Os 4 últimos colocados são: {tabela[-4:]}')
elif escolha == 3:
    print(f'A tabela em ordem alfabética fica assim {sorted(tabela)}')
elif escolha == 4:
    print(f'O Ceará está na {tabela.index("Ceará")+1}ª posição')
else:
    print('Opção inválida')
    
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)