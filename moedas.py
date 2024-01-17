# Módulo moedas para o desafio 107 a 110

# Este módulo guarda várias funções de aumentar, diminuir, dobro e metade, todos recebem o valor a ser
# trabalhado, aumentar e diminuir recebem um fator de cálculo.

# A função de metade recebe o valor a ser calculado e parâmetros de de incremento e decremento
# para usar as outras funções para realizar os cálculos e enfim imprimir o resumo de tudo, 
# formatado e organizado em uma lista.

def aumentar(valor, fator):
    """Esta função faz o aumento de valor, baseado na porcentagem desejada, retornando o valor
    aumentado arredondando com 2 casas decimais.
    :valor: Recebe o valor base a ser aumentado
    :fator: Recebe o fator para modificar o valor base, em porcentagem
    :return: Retorna o resultado de valor x fator, arredondado com 2 casas decimais
    """
    valorAumentado = valor+(valor*fator/100)
    return round(valorAumentado, 2)

def diminuir(valor, fator):
    """Esta função faz a diminuição de valor, baseado na porcentagem desejada, retornando o 
    valor reduzido arredondando com 2 casas decimais.
    :valor: Recebe o valor base a ser reduzido
    :fator: Recebe o fator para modificar o valor base, em porcentagem
    :return: Retorna o resultado de valor - (valor x fator), arredondado com 2 casas decimais
    """
    valorReduzido = valor-(valor*fator/100)
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

def resumo(valor, incremento, decremento):
    """A função recebe como parametros o valor a ser usado nos cálculos, e os de incremento e
    decremento a ser usados nas funções de cálculos, para imprimir a lista organizada com os 
    resultados obtidos de outras funções
    :valor: entrada de float que servirá de valor base para os cálculos
    :incremento: um valor de 0 a 100 de float para servir de fator de incremento
    :decremento: um valor de 0 a 100 de float para servir de fator de decremento
    """
    print('-'*35)
    print(f"{'RESUMO DO VALOR':^35}")
    print('-'*35)
    print(f"{'Preço analisado':<16} {moeda(valor):>16}")
    print(f"{'Dobro do preço':<16} {moeda(dobro(valor)):>16}")
    print(f"{'Metade do preço':<16} {moeda(metade(valor)):>16}")
    print(f"{incremento}{'% de aumento':<12} {moeda(aumentar(valor, incremento)):>16}")
    print(f"{decremento}{'% de redução':<12} {moeda(diminuir(valor, decremento)):>16}")
    print('-'*35)