# Nesse último algoritmo o desafio não foi fazer a função que faz as linhas e joga o input do
# usuário dentro da função help do Python, foi fazer o uso das cores, que eu já não lembrava
# mas revendo a última aula do mundo1 deu uma ajuda

# O algoritmo pega o termo que o usuário deseja pesquisar no 'help()' e coloca umas cores, 
# como uma máscara, deixando a interface mais amigável ao usuário


print('*' *30)
print(f"{'Python Mundo 3 - Desafio 106' :^30}")
print('*' *30)

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
    """Essa função pega o comando digitado pelo usuário e o coloca dentro do help(), realizando
    a pesquisa desejada, imprimindo o resultado usando a função titulo(), que coloca as cores
    definidas no texto.
    :param: comando: Termo a ser pesquisado no help()
    :return: Imprime o resultado da busca aplicando as cores determinadas na função titulo()
    """
    titulo(f"Acessando o manual do comando \'{comando}\'", 4)
    print(c[6], end='')
    help(comando)
    print(c[0], end='')
    sleep(2)
    
    
def titulo(mensagem, cor=0):
    """Essa função imprime as mensagens determinadas pelo programa, no ínicio, ao se realizar
    uma pesquisa e ao final do programa no encerramento, com as devidas formatações e cores
    estabelecidas previamente.
    """
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

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)