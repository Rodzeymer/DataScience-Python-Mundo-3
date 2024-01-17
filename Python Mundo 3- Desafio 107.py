# Estudando modularização, é um conceito simples de separar as funções dos programas principais
# facilitando a leitura, organização e manutenção dos códigos, permite reaproveitar as funções
# e reduz o tamanho dos códigos em projetos muito grandes.

# Nesse desafio devemos simplesmente criar funções em um arquivo possui as funções, nesse caso
# o arquivo moedas.py, e o outro arquivo, no caso esse, importa as funções e as usa para 
# executar os comandos.

# Isso é bem prático, quando se tem funções sendo usadas em programas diversos.


print('*' *30)
print(f"{'Python Mundo 3 - Desafio 107' :^30}")
print('*' *30)

from utilidades import moeda

valor = float(input('Digite o valor: R$'))

print(f"O valor R${valor} aumentado em 10% é R${aumentar(valor, 10)}")
print(f"O valor R${valor} reduzido em 13% é R${diminuir(valor, 13)}")
print(f"O valor R${valor} dobrado é R${dobro(valor)}")
print(f"O valor R${valor} pela metade é R${metade(valor)}")

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)