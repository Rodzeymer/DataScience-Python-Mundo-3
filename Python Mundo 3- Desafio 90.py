# Neste desafio 90 o uso de dicionários será interessante de se usar, já que é uma evolução das
# listas, adicionando uma nova dimensão à estrutura.

# Esse algoritmo deve receber o nome e a média de um aluno, salvando-os em um dicionário e depois
# lendo as informações salvas em um print, mostrando as informações de forma estruturada

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 90' :^30}")
print('*' *30)

aluno={}

aluno['nome'] = str(input(f"Digite o nome do aluno: "))
aluno['media'] = float(input(f"Digite a média de {aluno['nome']}: "))
if aluno['media'] >=7:
    aluno['final'] = "Aprovado"
else:
    aluno['final'] = "Reprovado"
print(f"O aluno {aluno['nome']} obteve média {aluno['media']} estando portanto {aluno['final']}.")

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30) 