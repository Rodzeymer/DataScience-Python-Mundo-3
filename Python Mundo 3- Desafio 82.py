# Neste desafio, também simples, é inclusive parecido com o anterior, nesse o algoritmo a ser 
# construído deve armazenar os números digitados pelo usuário, enquanto ele quiser, depois de 
# finalizado o programa deve separar os pares dos impares em duas outras listas.

# Então em um loop de True, o usuário vai digitando os números e os armazenando numa listas
# e continuando a continuar até que interrompa o loop com break, após o loop o programa vai
# analisar a lista e separar os números cujo resto da divisão por dois for igual à zero na 
# lista par e os outros na lista ímpar e exibiro as duas listas no encerramento da execução.

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 82' :^30}")
print('*' *30)
lista = []

while True:
    novoNumero = int(input('Digite um novo número'))
    lista.append(novoNumero)
    continuar = input('Quer continuar? [S/N]').lower()
    if continuar == 'n':
        break
pares = []
impares = []
for numeros in lista:
    if numeros%2 == 0:
        pares.append(numeros)
    else:
        impares.append(numeros)
        
print(f'Lista completa {lista}')
print(f'Lista de pares {pares}')
print(f'Lista de impares {impares}')


print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)