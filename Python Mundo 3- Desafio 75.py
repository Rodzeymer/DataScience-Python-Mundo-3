# Mais um desafio para consolidar os aprendizados em tuplas, agora o sistema vai perguntar 4
# vezes em um laço do tipo for por um número inteiro, verificar se foi digitado algum número 9, 
# a primeira aparição do número 3, se houver, quantos números pares foram inseridos e quais
# são eles, através do uso de vetores e tuplas. A cada repetição o algoritmo identifica e 
# separa os números ímpares, e ao final da tupla são identificadas a quantidade de noves, se 
# houve alguma ocorrência de 3 e qual a posição do primeiro 3, quantos números pares, através
# do tamanho do vetor de números pares e quais são eles, pelo próprio vetor.

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 75' :^30}")
print('*' *30)

lista = []
listaPar =[]
for c in range (0,4):
    numeroNovo = int(input(f'Digite o {c+1}º número'))
    if numeroNovo %2 == 0:
        listaPar.append(numeroNovo)
    lista.append(numeroNovo)
tupla = (lista[0], lista[1], lista[2], lista[3])
quantosNove = tupla.count(9)
print(f'Os números sorteados foram: {tupla}')
print(f'Apareceram {quantosNove} números 9')
if 3 not in tupla:
    print('Não há número três')
else:
    primeiroTres = tupla.index(3)
    print(f'O primeiro 3 aparece na posição {primeiroTres+1}')
print(f'Foram digitados {len(listaPar)} números pares')
print(f'Os números pares digitados foram {listaPar}')

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)