# O desafio é explorar algumas funcionalidades das tuplas, nesse é feito um sorteio de números
# de 0 a 5, inseridos em um vetor e depois convertido em uma tupla, adicionando os elementos
# na criação dessa tupla, após a criação da tulpa essa não pode ser alterada, mas a tupla 
# possui propriedadas que facilitam encontrar os números mais altos e os menores, conforme
# demonstrado por esse algoritmo

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 74' :^30}")
print('*' *30)

from random import randint
lista = []
for c in range (0,5):
    lista.append(randint(0,10))
tupla = (lista[0], lista[1], lista[2], lista[3], lista[4])

print(f'Os números sorteados foram: {tupla}')
print(f'O maior número sorteado foi: {max(tupla)}')
print(f'O menor número sorteado foi: {min(tupla)}')
    
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)