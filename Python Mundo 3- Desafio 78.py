#Quase lá


print('*' *30)
print(f"{'Python Mundo 3 - Desafio 78' :^30}")
print('*' *30)

lista = []
listaMaior =[]
listaMenor=[]
for c in range(0,5):
    novoNumero = int(input(f'Digite o número da posição {c}'))
    lista.append(novoNumero)


maiorNumero = max(lista)
listaMaior.append(lista.index(maiorNumero))
if lista.count(maiorNumero) >1:
    while len(listaMaior) <= lista.count(maiorNumero)-1:
        listaMaior.append(lista.index(maiorNumero, len(listaMaior)+1))
   
menorNumero = min(lista)
listaMenor.append(lista.index(menorNumero))
if lista.count(menorNumero) >1:
    while len(listaMenor) <= lista.count(menorNumero)-1:
        listaMenor.append(lista.index(menorNumero, len(listaMenor)+1))

print(f'Lista completa {lista}')
print(f'Maior valor {maiorNumero}')
print(f'Posição dos maiores valores {listaMaior}')
print(f'Menor valor {menorNumero}')
print(f'Posição dos menores valores {listaMenor}')

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)