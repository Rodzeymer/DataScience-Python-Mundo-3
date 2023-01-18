#Tá dificil


print('*' *30)
print(f"{'Python Mundo 3 - Desafio 78' :^30}")
print('*' *30)

lista = []
listaMaior =[]
listaMenor=[]
for c in range(0,5):
    novoNumero = int(input(f'Digite o número da posição {c}'))
    if len(lista) == 0:
        maiorNumero = menorNumero = novoNumero
    else:
        if novoNumero > maiorNumero:
            maiorNumero = novoNumero
        if novoNumero < menorNumero:
            menorNumero = novoNumero
    lista.append(novoNumero)
    
listaPosicao=enumerate(lista)
for maiorNumero, posicao in listaPosicao:
    print(listaPosicao.index(maiorNumero))


print(f'Lista padrão{lista}')
print(f'Lista enumerada {list(listaPosicao)}')
print(f'Maior numero {maiorNumero}')
print(f'Menor numero {menorNumero}')

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)