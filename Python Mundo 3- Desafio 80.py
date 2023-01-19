# Esse desafio também foi bem desafiador, mas a solução se mostrou mais simples que parecia ser 
# no princípio. Construir um algoritmo que peça ao usuário para digitar 5 números e inserí-los
# na posição correta dependendo de seu valor, sem usar sort ao final.

# O usuário é solicitado a inserir um valor, que será testado, sendo o primeiro valor ele será
# inserido no 'final' da lista, já que é o primeiro, valores maiores que o último serão coloca
# dos depois do último valor, e o último valor continua sendo o maior de todos, se o valor não 
# for maior que o maior valor da lista então é executado um teste que percorra toda a lista
# e encontre um valor que seja menor que o novo valor, ou que o primeiro cujo valor seja maior 
# que o novo valor, e então esse será a posição do novo valor, ao final o programa deve exibir 
# a lista completa, que deve estar na ordem crescente correta.

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 80' :^30}")
print('*' *30)

lista = []

for c in range(0,5):
    novoValor = int(input('Digite um valor'))
    if c == 0 or novoValor > lista[-1]:
        lista.append(novoValor)
        print(f'O valor {novoValor} foi adicionado no final da lista')
    else:
        posicao=0
        while posicao < len(lista):
            if novoValor <= lista[posicao]:
                lista.insert(posicao, novoValor)
                print(f'O valor {novoValor} foi adicionado na posição {posicao}')
                break
            posicao +=1
print(f'A lista inserida foi {lista}')


print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)