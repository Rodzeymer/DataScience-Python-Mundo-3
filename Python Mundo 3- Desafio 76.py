# Agora um programa simples pra usar um pouco sobre formatação das saídas, os prints,
# em python, com as f-strings conseguimos centralizar, alinha à esquerda ou à direita,
# completar espaço em branco com pontos e etc, incluindo cores. Aqui pegamos uma lista de 
# preços e formatamos, colocando, de dentro de uma tupla com o nome do produto e seu preço
# e fizemos um laço de repetição que executa um print para todos os itens, exibindo ao final 
# a lista formatada e bem mais agradável de se olhar

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 76' :^30}")
print('*' *30)

listagem = (['Lápis', 1.75], ['Borracha', 2.00], ['Caderno', 15.90], ['Estojo', 25.00], ['Transferidor', 4.20], ['Compasso', 9.99], ['Mochila', 120.32], ['Canetas', 22.30], ['Livro', 34.90])

print('-'*32)
print(f"{'LISTAGEM DE PREÇOS' : ^32}") 
print('-'*32)

for produto, preco in listagem:
    pontos='.'
    complemento = 20-len(produto)
    print(f'{produto} {pontos*complemento} R${preco:>6.2f}')
    
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)