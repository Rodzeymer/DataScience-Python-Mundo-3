# Continuando com os estudos de módulos e pacotes, vamos reaproveitar o código do Desafio 108

# Agora reaproveitando o código do Desafio 108, vamos importar mais um módulo com funções, 
# o emReal2, que traz a função que insere o valor float digitado no programa principal e 
# converte para uma string formatada para real brasileiro, com separador de milhar e duas casas
# decimais, agora com um novo parâmetro dizendo se a formatação ocorre ou não


print('*' *30)
print(f"{'Python Mundo 3 - Desafio 109' :^30}")
print('*' *30)

import moedas, emReal2

valor = float(input('Digite o valor: R$'))

print(f"O valor {valor} agora é {moeda2(valor, True)}")
print(f"O valor {moeda2(valor, True)} aumentado em 10% é {moeda2(aumentar(valor, 1.1), False)}")
print(f"O valor {moeda2(valor, False)} reduzido em 13% é {moeda2(diminuir(valor, 0.13), True)}")
print(f"O valor {moeda2(valor, True)} dobrado é {moeda2(dobro(valor), False)}")
print(f"O valor {moeda2(valor, False)} pela metade é {moeda2(metade(valor), True)}")

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)