from random import randint
lista = []
for c in range (0,5):
    lista.append(randint(0,10))
tupla = (lista[0], lista[1], lista[2], lista[3], lista[4])
valores = sorted(tupla)
print(f'Os números sorteados foram: {tupla}')
print(f'O maior número sorteado foi: {valores[-1]}')
print(f'O menor número sorteado foi: {valores[0]}')