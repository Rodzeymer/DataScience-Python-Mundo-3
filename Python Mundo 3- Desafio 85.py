# Pesquisando sobre listas, pode-se manipular listas aninhadas como elementos da lista-mãe.

# Então, o sistema construído recebe 7 números do usuário, os armazena em uma lista aninhada, colocandos
# os números pares em uma sublista e os ímpares em outra. Ao final ambas listas são ordenadas e impressas.


print('*' *30)
print(f"{'Python Mundo 3 - Desafio 84' :^30}")
print('*' *30)

listaCompleta = [[], []]

for numero in range(1,8):
    numeros = (int(input(f"Digite o {numero}° valor: ")))
    if numeros %2 == 0:
        listaCompleta[0].append(numeros)
    else:
        listaCompleta[1].append(numeros)
listaCompleta[0].sort()
listaCompleta[1].sort()
print(f"Lista Pares {listaCompleta[0]}")
print(f"Lista Impares {listaCompleta[1]}")

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)