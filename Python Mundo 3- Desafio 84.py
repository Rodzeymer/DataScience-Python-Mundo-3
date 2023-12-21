continuar = 's'
listaFinal = list()
listaPrevia = list()
listaMais = list()
listaMenos = list()
contador = 0

while continuar == 's':
    listaPrevia.append(str(input(f"Nome da pessoa número {contador}: ")))
    listaPrevia.append(int(input('Peso: ')))
    if contador == 0:
        menorPeso = listaPrevia[1]
        menorNome = listaPrevia[0]
        maiorPeso = listaPrevia[1]
        maiorNome = listaPrevia[0]
        print(f"A pessoa cadastra de maior peso foi {maiorNome} com {maiorPeso}Kg")
        print(f"A pessoa cadastra de menor peso foi {menorNome} com {menorPeso}Kg")

    if contador>=1:
        if listaPrevia[1] <= menorPeso:
            menorPeso = listaPrevia[1]
            menorNome = listaPrevia[0]
            listaMenos.append(listaPrevia[0])
            listaMenos.append(listaPrevia[1])
        if listaPrevia[1] >= maiorPeso:
            maiorPeso = listaPrevia[1]
            maiorNome = listaPrevia[0]
            listaMais.append(listaPrevia[0])
            listaMais.append(listaPrevia[1])
        print(f"A pessoa cadastra de maior peso foi {maiorNome} com {maiorPeso}Kg")
        print(f"A pessoa cadastra de menor peso foi {menorNome} com {menorPeso}Kg")
    listaFinal.append(listaPrevia[:])
    contador = contador + 1
    listaPrevia.clear()
    continuar = input('Quer continuar? [S/N]').lower()
    if continuar == 'n':
        break
print(f"Foram cadastradas {contador} pessoas!")
print(f"A pessoa cadastra de maior peso foi {listaMais}")
print(f"A pessoa cadastra de menor peso foi {listaMenos}")
print(listaFinal)