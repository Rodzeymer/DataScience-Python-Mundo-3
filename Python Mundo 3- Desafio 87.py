# Com o desafio 86 feito e esse sendo baseado nele ficou fácil, com alguns testes ficou tudo certo.

# O algoritmo deve solicitar ao usuário 9 valores e organizá-los em uma matriz 3x3, colocando os valores
# em sua respectiva posição de linha e coluna, mas exibindo algumas informações dessa matriz, como a 
# soma dos números pares, a soma dos valores que estão na terceira coluna e o maior valor da segunda linha, 
# com isso já extraindo algumas informações dessa matriz de dados.

matriz = [[0,0,0], [0,0,0], [0,0,0]]
somaPares=0
somaTerceira = 0
maiorValorSegunda = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um valor para o endereço {l}, {c}"))
        if matriz[l][c] %2 == 0:
            somaPares = somaPares+matriz[l][c]
        if c == 2:
            somaTerceira = somaTerceira+matriz[l][c]
        if l == 1:
            if matriz[l][c] > maiorValorSegunda:
                maiorValorSegunda = matriz[l][c] 
            
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end='')
    print()
print('*' *30)
print(f"A soma de todos os valores pares é {somaPares}")
print(f"A soma dos valores da terceira coluna é {somaTerceira}")
print(f"O maior valor da segunda linha é {maiorValorSegunda}")

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)