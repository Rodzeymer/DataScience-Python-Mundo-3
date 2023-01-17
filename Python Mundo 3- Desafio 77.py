# Neste desafio foi proposto um algoritmo que, dada palavra, sejam identificadas as suas
# vogais, então uma tupla foi inserida e o algortimo faz um loop para cada palavra nessa tupla
# e para cada palavra ele faz um loop por todas os characteres, se for identificado alguma 
# vogal o sistema faz uma cópia dela para a lista de vogais que é apresentado ao final de cada
# iteração de palavra

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 77' :^30}")
print('*' *30)

lista = ('Brasil', 'Russia', 'India', 'China', 'South Africa')

for palavra in lista:
    vogais = []
    tupla = tuple(palavra)
    for letra in range (0, len(tupla)):
        if tupla[letra] in 'AaEeIiOoUu':
            vogais.append(tupla[letra])
    print(f'Na palavra {palavra} há as vogais{vogais}')
    
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)