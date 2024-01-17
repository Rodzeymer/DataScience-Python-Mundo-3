# Módulo moedas para o desafio 108

# Este módulo guarda a função de formatação de valores para o real brasileiro, juntamente com 
# o separador de milhar

def moeda(valor):
    """Essa função pega o valor inserido no sistema e retorna ele com uma formatação próxima
    da usada normalmente, com o síbolo de Real na frente, separador de milhar e arredondado
    par 2 casas decimais, que no caso seriam os reais.
    :valor: valor a ser manipulado em float
    :return: a saída em string
    """
    emReal = str(f"R${valor:,.2f}")
    return emReal