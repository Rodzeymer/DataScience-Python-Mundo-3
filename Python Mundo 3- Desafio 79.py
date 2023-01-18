# Neste desafio de listas o algoritmo deve permitir que o usuário insira quantos números quiser
# mas impeça a inclusão de números repetidos, solicitando se o usuário quer continuar.

# O algoritmo solicita a entrada e testa se o valor inserido já ocorreu na lista, em caso
# positivo ele exibe uma mensagem de número repetido, se não ele insere o número novo na 
# lista e pergunta ao usuário se ele que continuar. Caso o usuário queira encerrar o loop é 
# interrompido, a lista organizada e exibida ao final.

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 79' :^30}")
print('*' *30)

lista = []
while True:
    novoValor = int(input('Digite um novo valor'))
    if novoValor in lista:
        print(f'Desculpe, o valor {novoValor} já está na lista')
    else:
        lista.append(novoValor)
    continuar = input('Quer continuar? [S/N]').upper()
    if continuar == 'N':
        break
lista.sort()  
print(f'Os números inseridos foram {lista}')

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)