# Neste desafio pegamos a função leiaInt() do desafio 104 e fiz um tratamento de erros nele
# incluindo uma função que valida entrada float e ao final uma função que reune os dados válidos
# da leiaInt()) e da leiaFloat()

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 113' :^30}")
print('*' *30)

def leiaInt(numInteiro=0):
    """Essa função solicita a entrada do usuário pedindo que seja inserido um valor numérico
    inteiro, rejeitando outras entradas apresentando mensagens de erro personalizadas, até que
    seja feita a entrada de um número inteiro.
    :numInteiro: Entrada genérica de dado
    :return = i: retorna o valor da variável validada como inteiro.
    """
    inteiro=False
    try:
        while inteiro == False:
            i=str(input(numInteiro))
            if i.isdigit() == True:
                inteiro=True
                return i
            else:
                print('Erro: digite um valor inteiro')
    except KeyboardInterrupt:
        print(f"O usuário não informou os dados")
        
        
def leiaFloat(numDecimal=0):
    """Essa função solicita a entrada do usuário pedindo que seja inserido um valor numérico
    decimal, rejeitando outras entradas apresentando mensagens de erro personalizadas, até que
    seja feita a entrada de um número decimal.
    :numInteiro: Entrada genérica de dado
    :return = d: retorna o valor da variável validada como decimal.
    """
    decimal=False
    try:
        while decimal == False:
            d=str(input(numDecimal))
            try:
                float(d)
                return d
                decimal = True
            except ValueError:
                print('Erro: digite um valor real')
    except KeyboardInterrupt:
        print(f"O usuário não informou os dados")
        
        
def resultado(i, d):
    """Essa função reúne os resultados de leiaInt() e leiaFloat() e imprime uma saída persona-
    lizada das duas funções.
    :i: Dado validado como inteiro
    :d: Dado validado como decimal
    :return: Imprime uma mensagem contendo os números validados
    """
    print(f"Você digitou inteiro: {i} e decimal: {d}")
    
i = leiaInt('Digite um Inteiro: ')
d = leiaFloat('Digite um Real: ')
resultado(i, d)

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)