# Agora em funções apredi a usar o comando hrlp(), inclusive adicionando as def strings, pra 
# ajudar a documentar melhor as funções, pois no futuro alguma das minhas funções autorais 
# sejam usadas por terceiros, então é sempre bom documentar tudo direito para não deixar 
# trabalho pela metade.

# A partir desse algoritmo farei uso das def string pra detalhar mais a função, seus argumentos
# e resultados. A função voto() pega o ano de nascimento de uma pessoa a ser analisada e calcula
# sua idade para então devovler como retorno uma frase explicando a situação dessa pessoa com 
# nome idade e situação eleitoral.

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 101' :^30}")
print('*' *30)

from datetime import date

def voto(nascimento):
    """
    Essa função pega o ano de nascimento da pessoa e retorna se essa pessoa tem como 
    condição de voto: Obrigatório, Opcional, ou Negado
    :param: nascimento: ano de nascimento da pessoa analisada
    :return: Dependendo da idade retorna se o voto é negado, opcional ou obrigatório
    """
    
    anoAtual = date.today().year
    idade = anoAtual - nascimento
    if idade <16:
        return print(f"Com {idade} anos, {nome} é muito novo, tendo seu direito ao voto NEGADO")
    if idade >=16 and idade <18 or idade >65:
        return print(f"Com {idade} anos, {nome} está na idade em que o voto é FACULTATIVO")
    if idade >=18:
        return print(f"Com {idade} anos, {nome} atingiu a maioridade, seu voto é OBRIGATÓRIO")
        
nome = str(input("Digite o nome da pessoa a ser analisada"))
nascimento = int(input(f"Digite o ano de nascimento de {nome}"))
voto(nascimento)

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)