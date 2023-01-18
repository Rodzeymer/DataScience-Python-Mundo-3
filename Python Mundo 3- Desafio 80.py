# 

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 80' :^30}")
print('*' *30)

lista = []

for c in range(0,5):
    novoValor = int(input('Digite um valor'))
    if len(lista) == 0:
        print(f'{novoValor} é o primeiro valor inserido na lista')
        lista.append(novoValor)
    else:
        listaMax = max(lista)
        listaMin = min(lista)
        print(f'Máximo {listaMax}')
        print(f'Mínimo {listaMin}')
        if novoValor>listaMax:
            lista.append(novoValor)
            print(f'O {novoValor} foi adicionado na posição {lista.index(novoValor)}')
        if novoValor<listaMin:
            lista.insert(0, novoValor)
            print(f'O {novoValor} foi adicionado na posição {lista.index(novoValor)}')
            
        
print(f'A lista inserida foi {lista}')


print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)