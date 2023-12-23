# Depois de pesquisar na documentação um pouco encontrei uma solução simples mas que não me deixou
# satisfeito, mas antes feito que perfeito.

# O sistema construído deve solicitar nome e peso de n pessoas, sempre perguntando ao usuário se ele
# deseja continuar e solicitar as informações até que o usuário escolha não continuar a inserir novas
# informações. O algoritmo reserva essa informações em uma lista prévia, lançando-as em uma lista final, 
# resetando a lista prévia, contando quantas inserções foram feitas, e ao final da última iteração, 
# o sistema avalia qual foram os pesos máximos e mínimos, sem alterar a ordem da lista final e imprimindo
# na tela quantas inserções foram feitas, os pesos máximos e mínimos, com seus respectivos nomes e 
# imprime a lista final por último.

# PS. Depois de ver a solução dp Guanabara decidi implementar o final por questões estéticas, mas o restante
# continua autoral, agora fiquei satisfeito!

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 84' :^30}")
print('*' *30)

continuar = 's'
listaFinal = list()
listaPrevia = list()

contador = 0

while continuar == 's':
    listaPrevia.append(str(input(f"Nome da pessoa número {contador}: ")))
    listaPrevia.append(float(input('Peso: ')))
    listaFinal.append(listaPrevia[:])
    contador = contador + 1
    listaPrevia.clear()
    continuar = input('Quer continuar? [S/N]').lower()
    if continuar == 'n':
        maior=max(listaFinal, key=lambda item: item[1])
        menor=min(listaFinal, key=lambda item: item[1])
        break
print(f"Foram cadastradas {contador} pessoas!")
print(f"O maior peso foi de {maior[1]}kg.", end='')
for p in listaFinal:
    if p[1] == maior[1]:
        print(f"[{p[0]}] ", end='')
print()
print(f"O menor peso foi de {menor[1]}kg.", end='')
for p in listaFinal:
    if p[1] == menor[1]:
        print(f"[{p[0]}] ", end='')
print()

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)