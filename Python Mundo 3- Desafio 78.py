# Esse desafio, foi um Desafio com D maiúsculo, mas foi vencido. Construir um algoritmo que 
# pegue os cinco números que o usuário digitar, coloque numa lista, e exiba, além da lista 
# inteira o maior e o menor número e suas respectivas posições, mesmo que o máximo e o mínimo
# se repita, mostrar as posições de todas as suas posições

# O algortimo pega os números e vai alimentando a lista, depois pega o máximo e os mínimos dela 
# e joga em uma variável, testa para ver se eles, max e min, se repetem, se houver repetição o
# programa verifica, após a ocorrência do primeiro, a posição dos demais e alimenta uma lista,
# uma de posição dos máximos e outra dos mínimos, para então apresentar ao final da execução

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 78' :^30}")
print('*' *30)

lista = []
listaMaior =[]
listaMenor=[]
for c in range(0,5):
    novoNumero = int(input(f'Digite o número da posição {c}'))
    lista.append(novoNumero)

print(f'A lista completa: {lista}')
maiorNumero = max(lista)
menorNumero = min(lista)
if maiorNumero == menorNumero:
    print(f'O maior e menor valor é o mesmo: {maiorNumero}')
else:
    print(f'O número de maior valor: {maiorNumero}')
    print(f'O número de menor valor: {menorNumero}')
    
listaMaior.append(lista.index(maiorNumero))
if lista.count(maiorNumero) > 1 and lista.count(maiorNumero) < len(lista):
    while len(listaMaior) <= lista.count(maiorNumero)-1:
        listaMaior.append(lista.index(maiorNumero, len(listaMaior)+1))
    print(f'Posição dos maiores valores {listaMaior}')
elif lista.count(maiorNumero) == 1:
    print(f'A posição do maior valor é: {listaMaior}')
elif lista.count(maiorNumero) == len(lista):
    print('A lista apresenta apenas 1 valor')
listaMenor.append(lista.index(menorNumero))
if lista.count(menorNumero) > 1 and lista.count(menorNumero) < 4:
    while len(listaMenor) <= lista.count(menorNumero)-1:
        listaMenor.append(lista.index(menorNumero, len(listaMenor)+1))
    print(f'Posição dos menores valores {listaMenor}')
elif lista.count(menorNumero) == 1:
    print(f'A posição do menor valor é: {listaMenor}')
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)