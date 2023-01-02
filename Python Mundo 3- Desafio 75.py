lista = []
numerosPar = 0
for c in range (0,4):
    numeroNovo = int(input(f'Digite o {c+1}º número'))
    if numeroNovo %2 == 0:
        numerosPar = numerosPar+1
    lista.append(numeroNovo)
tupla = (lista[0], lista[1], lista[2], lista[3])
quantosNove = tupla.count(9)
if 3 not in tupla:
    primeiroTres = 'Não há tres'
else:
    primeiroTres = tupla.index(3)
print(f'Os números sorteados foram: {tupla}')
print(f'Apareceram {quantosNove} números 9')
if 3 not in tupla:
    print('Não há número três')
else:
    primeiroTres = tupla.index(3)
    print(f'O primeiro 3 aparece na posição {primeiroTres}')
print(f'Foram digitados {numerosPar} números pares')