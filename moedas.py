# Módulo moedas para o desafio 107 e 108

# Este módulo guarda funções de aumentar, diminuir, dobro e metade, todos recebem o valor a ser
# trabalhado, aumentar e diminuir recebem um fator de cálculo.

def aumentar(valor, fator):
    """Esta função faz o aumento de valor, baseado na porcentagem desejada, retornando o valor
    aumentado arredondando com 2 casas decimais.
    :valor: Recebe o valor base a ser aumentado
    :fator: Recebe o fator para modificar o valor base, em porcentagem
    :return: Retorna o resultado de valor x fator, arredondado com 2 casas decimais
    """
    valorAumentado = valor*fator
    return round(valorAumentado, 2)

def diminuir(valor, fator):
    """Esta função faz a diminuição de valor, baseado na porcentagem desejada, retornando o 
    valor reduzido arredondando com 2 casas decimais.
    :valor: Recebe o valor base a ser reduzido
    :fator: Recebe o fator para modificar o valor base, em porcentagem
    :return: Retorna o resultado de valor - (valor x fator), arredondado com 2 casas decimais
    """
    valorReduzido = valor-(valor*fator)
    return round(valorReduzido, 2)
    
def dobro(valor):
    """Esta função faz a dobra do valor, retornando o valor dobradi arredondando com 
    2 casas decimais.
    :valor: Recebe o valor base a ser dobrado
    :return: Retorna o resultado do valor dobrado, arredondado com 2 casas decimais
    """
    valorDobrado = valor*2
    return round(valorDobrado, 2)

def metade(valor):
    """Esta função faz a reduz pela o valor, retornando a metade do valor arredondando com 
    2 casas decimais.
    :valor: Recebe o valor base a ser reduzido em 50%
    :return: Retorna o resultado da metade do valor, arredondado com 2 casas decimais
    """
    valorMetade = valor/2
    return round(valorMetade, 2)