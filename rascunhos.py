from time import sleep

c = ('\033[m',       #0 - Sem cores
     '\033[0;30;41m', #1 - Vermelho
     '\033[0;30;42m', #2 - Verde
     '\033[0;30;43m', #3 - Amarelo
     '\033[0;30;44m', #4 - Azul
     '\033[0;30;45m', #5 - Roxo
     '\033[7;30m'    #6 - Branco
    );

def ajudaInterativa(comando):
    titulo(f"Acessando o manual do comando \'{comando}\'", 4)
    print(c[6], end='')
    help(comando)
    print(c[0], end='')
    sleep(2)
    
    
def titulo(mensagem, cor=0):
    tamanho = len(mensagem) + 4
    print(c[cor], end='')
    print('~'*tamanho)
    print(f"  {mensagem}")
    print('~'*tamanho)
    print(c[0], end='')
    sleep(1)
    
    
while True:
    titulo('Sistema de ajuda do Python', 2)
    comando = str(input('Função ou Biblioteca> '))
    if comando.upper() =="FIM":
        break
    else:
        ajudaInterativa(comando)

titulo('Encerrando programa', 1)
    