# Esse desafio, na verdade nessa primeira parte do Desafio 115, reuniu muito do conhecimento dos
# mundos 2 e 3 de Python, tendo que criar novas funções e reaproveitando outras já feitas, para
# que o sistema proposto funcione corretamente.

# Primeiro criamos a função linhas() que imprime uma linha divisória, que funciona junto com a
# função cabeçalho para construir os cabeçalhos dos sistemas de forma padronizada, em seguida 
# temos o reaproveitamento a função leiaInt() do desafio 113 dentro de uma nova função que é a 
# função menu() que imprime o menu com o auxílio da função cabeçalho e solicita uma entrada do
# usuário, qual a opção do menu, e a valida com o uso da função leiaInt(), imprimindo o nome 
# da opção como cabeçalho.

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 115a' :^30}")
print('*' *30)

from time import sleep

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
    

def leiaInt(numInteiro):
    """Essa função solicita a entrada do usuário pedindo que seja inserido um valor numérico
    inteiro, rejeitando outras entradas apresentando mensagens de erro personalizadas, até que
    seja feita a entrada de um número inteiro.
    :numInteiro: Entrada genérica de dado
    :return = i: retorna o valor da variável validada como inteiro.
    """
    while True:
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


while True:
    resposta = menu(['Criar Arquivo','Cadastrar Pessoas','Listar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        cabeçalho('Criar Arquivo')
    elif resposta == 2:
        cabeçalho('Cadastrar Pessoas')
    elif resposta == 3:
        cabeçalho('Listar Pessoas') #583072997 
    elif resposta == 4:
        cabeçalho('Sair do Sistema')
        break
    else: 
        print('ERRO! Digite uma opção válida')
    sleep(2)

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)