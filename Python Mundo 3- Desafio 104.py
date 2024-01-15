# Tentando tratamento de erros

def leiaInt(entrada):
    """Pega a entrada inserida pelo usuário e tenta transformar em integer, e verifica e trata
    o erro, re-iniciando o algoritmo se mão conseguir transformar
    :entrada: entrada são tipada do usuário
    """
    while True:
        try:
            numero = int(entrada)
            if type(numero) == int:
                print('Entrada ok')
                break
            else:
                print('Entrada não ok')
        except ValueError as error:
            print('Deu erro de valor')
entrada = input('Digite algo')
leiaInt(entrada)