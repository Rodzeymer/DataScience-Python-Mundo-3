# Neste módulo dado temos a função de validação dos dados para o Desafio 112

# Esse desafio foi bem dificil pois dependendo de como se constrói a função pode ficar 
# solicitando a entrada duas vezes ou ficar em loop infinito e é dificil perder o hábito de se 
# tipar as entradas logo na solicitação do input.

# Esta função pega o dado informado pelo usuário e verifica se o mesmo é alfa numérica, se for
# ela retorna uma mensagem de erro e solicita uma nova entrada até que sejam dados numéricos 
# apenas. Quando essa entrada é validada retorna como float para ser usado por outras funções.

def leiaDinheiro(msg):
    """A função solicita uma entrada, então não é necessário solicitar input para jogar na 
    função, crie uma variável de input genérica que ela irá converter essa entrada para um 
    float, podendo já ser inserida como parâmetro de outra função que aceite o float.
    A função leiaDinheiro verifica se o input é composto por apenas números, se tiver letras
    ela exibe mensagem de erro e solicita novamente uma entrada numérica. Sendo inserida, essa 
    entrada numérica ela valida e a converte em float, retornando em float para uma possível
    função.

    :msg: input genérico que será convertido em string para validar isalpha(), em sendo alpha
    ele exibe mensagem de erro e solicita nova entrada
    :return: Sendo o input um valor numérico, esse é convertido em float e jogado pra fora da
    função.
    """
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f"ERRO: \"{entrada}\" é um valor inválido!")
        else:
            valido = True
            return float(entrada)
        
