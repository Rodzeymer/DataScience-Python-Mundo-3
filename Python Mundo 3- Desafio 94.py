# Mais um desafio que realmente foi desafiador, novamente testando capacidades de organização, 
# pois tem que ser definidos locais de entrada de dados, quais dados manipular e como manipular
# e as respostas, os outputs, do sistema, para que fique organizado e só exibindo os dados
# que constam no algoritmo, deixando de fora respostas vazias quando alguns dados não são
# inseridos.

# Esse algoritmo deve receber nome, sexo e idade de tantos cadastros quanto o usuário quiser 
# realizar, e ao final deve exibir:
    # A: Quantas pessoas foram cadastradas;
    # B: A média de idade do grupo;
    # C: Uma lista com todas as mulheres;
    # D: Uma lista com todas as pessoas com idade acima da média.

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 94' :^30}")
print('*' *30)

contador = 0
pessoa = {}
galera = []
totalIdade = 0
mulheres = []
maiorIdade = []

while True:
    contador = contador + 1
    pessoa['Nome'] = str(input(f"Digite o nome da pessoa {contador}"))
    pessoa['Sexo'] = str(input(f"Qual o sexo de {pessoa['Nome']}? [M/F]"))
    pessoa['Idade'] = int(input(f"Qual a idade de {pessoa['Nome']}"))
    totalIdade = totalIdade + pessoa['Idade']
    if pessoa['Sexo'] in 'Ff':
        mulheres.append(pessoa['Nome'])
    galera.append(pessoa.copy())
    continuar = str(input('Quer continuar? "S/N"'))
    if continuar in 'Nn':
        break
print(f"A: Foram cadastradas {contador} pessoas")
mediaIdade = totalIdade/contador
print(f"B: Média de idade do grupo cadastrado {mediaIdade:0.0f}")
if len(mulheres)>0:
    print(f"C: Foram cadastradas as seguintes mulheres {mulheres}")
for c in range(0, contador):
    if galera[c]['Idade'] > mediaIdade:
        maiorIdade.append(galera[c]['Nome'])
if len(maiorIdade)>0:
    print(f"D: Pessoas acima da média do grupo: {maiorIdade}")
    
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)