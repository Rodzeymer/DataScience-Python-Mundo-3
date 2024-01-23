# Parte 2 do Desafio 115, o 115b!

# 

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 115b' :^30}")
print('*' *30)

from time import sleep

#COMEÇO DAS FUNÇÔES#
def linhas(tam=45):
    """Essa função tem a função simples de imprimir uma linha composta por 45 traços, para ser
    usado como linhas separadoras nos cabeçalhos.
    :return: retorna uma linha com 45 traços
    """
    return '-' * tam
    
def cabeçalho(txt):
    """Essa função pega a linha da função linhas() e coloca um texto centralizado no meio de 
    duas linhas.
    :parametro txt: É a entrada do texto que irá ficar centralizado e entre as linhas
    :return: Os prints com o cabeçalho construido.
    """
    print(linhas())
    print(txt.center(42))
    print(linhas())
    

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
                numInteiro = int(i)
                return numInteiro
            else:
                print('Erro: digite um valor inteiro')
    except KeyboardInterrupt:
        print(f"O usuário não informou os dados")

def menu(listaOpcoes):
    """Lista as opções do Menu Principal com a formatação configurada pelo sistema, após isso 
    é solicitado ao usuário a entrada de uma das opções, sendo retornada a impressão do menu
    correspondente.
    :paramêtro listaOpcoes: pega as opções para imprimir a lista de opções
    :return: retorna a resposta solicitada pelo sistema para imprimir a opção desejada, validada
    pela função leiaInt()
    """
    cabeçalho('Menu Principal')
    contador = 1
    for item in listaOpcoes:
        print(f"  {contador} - {item}")
        contador+=1
    print(linhas())
    resposta = leiaInt('Sua opção: ')# desafio 113
    return resposta
    
cabeçalho('Sistema de Arquivo 3.14p')

def arquivoExiste(nomeArquivo):
  """A função verifica se o aruivo chamado existe, tentando abrí-lo, se não conseguir exibe
  uma mensagem de erro, se conseguir o fecha e exibe uma mensagem de arquivo encontrado
  :param arquivoNome: recebe o nome do arquivo a ser testado
  :return: Se não encontrar o arquivo retorna False
  """
  try:
    arquivoAbre = open(nomeArquivo, 'rt')
    arquivoAbre.close()
  except FileNotFoundError:
    return False
  else:
    print('Arquivo encontrado!')
    

def criarArquivo(nomeArquivo):
  """Caso queira, um arquivo pode ser criado, com o nome dele sendo informado pelo sistema, o 
  arquivo é fechado então, pode 
  """
  try:
    arquivoNovo = open(nomeArquivo, 'wt+')
    arquivoNovo.close()
  except:
    print('Houve um ERRO na criação do arquivo')


def lerArquivo(nomeArquivo):
  """
  """
  try:
    arquivoAbre = open(nomeArquivo, 'rt')
  except:
    print('Erro ao ler o arquivo')
  else:
    cabeçalho('Pessoas Cadastradas')
    print(arquivoAbre.readlines())
#FIM DAS FUNÇÕES#

#COMEÇO DO PROGRAMA PRINCIPAL#

while True:
    resposta = menu(['Criar Arquivo','Cadastrar Pessoas','Listar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um Arquivo
        lerArquivo(nomeArquivo)
    elif resposta == 2:
        cabeçalho('Cadastrar Pessoas')
    elif resposta == 3:
        cabeçalho('Listar Pessoas')
    elif resposta == 4:
        cabeçalho('Sair do Sistema')
        break
    else: 
        print('ERRO! Digite uma opção válida')
    sleep(2)
#FIM DO PROGRAMA PRINCIPAL#