# Tentando tratamento de erros, mas no final foi só pegar a entrada como string e testar se
# ela é numérica com a função isnumeric, tentei de outra forma mas essa foi o jeito que deu 
# certo

# O usuário simplesmente digita algo e manda para a função, sendo um dado numérico inteiro ele
# aceita a informação, se não ele exibe uma mensagem de erro e solicita novamente a entrada
# do usuário.


print('*' *30)
print(f"{'Python Mundo 3 - Desafio 104' :^30}")
print('*' *30)

def leiaInt(digito):
    """Pega a entrada inserida pelo usuário e tenta transformar em integer, e verifica e trata
    o erro, re-iniciando o algoritmo se mão conseguir transformar
    :entrada: entrada são tipada do usuário
    :return: Se foi inserido um valor numérico inteiro ou não
    """
    ok = False
    valor = 0
    while True:
        n=str(input(digito))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[0;31mErro Digite um número inteiro válido\033[m")
        if ok:
            break
    return valor

n = leiaInt('Digite um número: ')
print(f"Você acabou de digitar o número {n}!")

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)  