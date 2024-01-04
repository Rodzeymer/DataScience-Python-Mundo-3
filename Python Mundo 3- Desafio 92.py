# O desafio foi interessante de resolver, pois o uso de dicionários facilita a entrada de dados,
# podendo adicionar novos itens ao dicionário de forma direta, sem necessidade de comando para 
# isso, ficando mais organizado, já que a a chave pode ser palavra, facilitando a roganização 
# dos dados no programa

# Esse algoritmo deve solicitar nome, ano de nascimento (mas calcular a idade para guardar) e 
# CTPS, não possuindo CTPS a entrada de dados se encerra e procede-se a impressão dos dados.
# Mas havendo CTPS, se informa o número da carteira, o ano de contratação, o salário e com 
# quantos anos a pessoa cadastrada irá se aposentar. Tudo formatado no final acessando o 
# dicionário.

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 92' :^30}")
print('*' *30)

from datetime import date
import time

cadastro = {}

cadastro['Nome'] = str(input("Digite o nome: "))
nascimento= int(input(f"Digite o ano de nascimento de {cadastro['Nome']}: "))
anoAtual = date.today().year
cadastro['Idade'] = anoAtual - nascimento
cadastro['CTPS'] = int(input(f"Digite o número da carteira de trabalho de {cadastro['Nome']}: (0 - se não estiver empregado"))

if cadastro['CTPS'] == 0:
    empregado = False
else:
    empregado = True
    cadastro['Contratação'] = int(input(f"Digite o ano de contratação de {cadastro['Nome']}: "))
    cadastro['Salario'] = float(input(f"Digite o salário de {cadastro['Nome']}: "))
    tempoContratado = anoAtual - cadastro['Contratação']
    cadastro['Aposentadoria'] = cadastro['Idade']-(tempoContratado - 35)

print('Calculando dados e formatando saída')
time.sleep(1.5)
print(f"O nome cadastrado foi: {cadastro['Nome']}")
print(f"A idade de {cadastro['Nome']} é {cadastro['Idade']}")
if empregado == True:
    print(f"{cadastro['Nome']} possui CTPS de número {cadastro['CTPS']}")
    print(f"Contratado desde {cadastro['Contratação']}, {cadastro['Nome']} irá se aposentar com {cadastro['Aposentadoria']} anos")
else:
    print(f"Como {cadastro['Nome']} está sem emprego não irá se aposentar tão cedo")

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)