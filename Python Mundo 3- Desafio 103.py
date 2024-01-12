# Usando funções com parametros opcionais, apenas parametros strings são opcionais, os 
# parametros integer NECESSITAM receber um parametro no seu input, mas na função pode-se parsear
# a variável e transformar em int.

# Esse algoritmo pega um nome e a quantidade de gols informados pelo usuário, imprimindo através
# da função uma frase utilizando esses dados, ou se não for inserido os dados necessários a
# função ainda irá imprimir, uma frase com parâmetros padrões, a serem utilizados em caso de 
# não terem sido inseridos pelo usuário.

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 103' :^30}")
print('*' *30)

def ficha(nome, gols):
    """ Essa função pega as strings de nome e gols do jogador para imprimir o retorno com a
    frase configurada, verificando primeiramente se ambos os parametros estão vazios, aplicando
    um valor padrão, no parametro gols ainda converte a string em integer.
    :param: nome: string que informa o nome do jogador
    :param: gols: string que informa a quantidade de gols, parseado em integer 
    :return: imprime a mensagem com o nome e gols do jogador informado
    """
    if nome == '':
        nome = ('<Desconhecido>')
    if gols == '':
        gols = int(0)
    else:
        gols = int(gols)
    return print(f"O jogador {nome} fez {gols} gol(s) no campeonato")
    
nome = str(input('Digite o nome do jogador.'))
gols = str(input('Digite o número de gols'))

ficha(nome, gols)

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)  