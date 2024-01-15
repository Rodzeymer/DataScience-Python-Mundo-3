# Tentando tratamento de erros


print('*' *30)
print(f"{'Python Mundo 3 - Desafio 104' :^30}")
print('*' *30)

def leiaInt(entrada):
    """Pega a entrada inserida pelo usuário e tenta transformar em integer, e verifica e trata
    o erro, re-iniciando o algoritmo se mão conseguir transformar
    :entrada: entrada são tipada do usuário
    :return: Se foi inserido um valor numérico inteiro ou não
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

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)  