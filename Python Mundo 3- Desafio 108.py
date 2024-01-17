# Continuando com os estudos de módulos e pacotes, vamos reaproveitar o código do Desafio 107

# Agora reaproveitando o código do Desafio 107, vamos importar mais um módulo com funções, 
# o emReal, que traz a função que insere o valor float digitado no programa principal e 
# converte para uma string formatada para real brasileiro, com separador de milhar e duas casas
# decimais.


print('*' *30)
print(f"{'Python Mundo 3 - Desafio 108' :^30}")
print('*' *30)

import moedas, emReal

valor = float(input('Digite o valor: R$'))

print(f"O valor {valor} agora é {moeda(valor)}")
print(f"O valor {moeda(valor)} aumentado em 10% é {moeda(aumentar(valor, 10))}")
print(f"O valor {moeda(valor)} reduzido em 13% é {moeda(diminuir(valor, 13))}")
print(f"O valor {moeda(valor)} dobrado é {moeda(dobro(valor))}")
print(f"O valor {moeda(valor)} pela metade é {moeda(metade(valor))}")

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)