# Usando duas funções é possível usar o resultado de uma para outra e obter resultados mais
# complexos e trabalhados.

# Nesse programa o sistema sorteia 5 números na primeira função e os coloca em uma lista, para
# que a segunda função pegue essa lista e faça a soma dos números pares dessa lista, imprimindo
# os resultados ao final de cada função.

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 100' :^30}")
print('*' *30)

import random, time
lista = []

def sorteio():
    for contador in range (0, 5):
        lista.append(random.randint(0, 100))
    print(f"Sorteando 5 valores da lista: {lista}.")


def somaPar(lista):
    soma  = 0
    for n in lista:
        if n%2==0:
            soma=soma+n
    print(f"Somando os valores pares de {lista}.")
    time.sleep(0.6)
    print(f"O resultado foi {soma}.")
            
            
sorteio()
somaPar(lista)

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)