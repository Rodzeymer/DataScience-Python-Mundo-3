# Continuando com os estudos de módulos e pacotes, vamos reaproveitar o código do Desafio 110

# Agora reaproveitando o código do Desafio 110, vamos pegar a função construída em dado, que irá
# fazer a validação dos dados inseridos, verificando se são numéricos ou letras, após essa
# validação, os dados serão inseridos na função resumo realizando os cálculos, mas agora com
# dados validados como float, evitando que o algoritmo pare de ter seu funcionamento interrompido
# por conta de erro por não ter sido informados dados que não sejam do tipo float.

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 112' :^30}")
print('*' *30)

from utilidades import moeda, dado

valor = dado.leiaDinheiro('Digite o valor a ser usado')
incremento = dado.leiaDinheiro('Digite o incremento')
decremento = dado.leiaDinheiro('Digite o decremento')

moeda.resumo(valor, incremento, decremento)

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)