# Começamos o Mundo 3 já relembrando muito do que foi aprendido até aqui, vetores, estrutura de
# loop, condicionais, condição de parada e então o desafio é, construir um algoritmo que pegue
# um número inteiro de 0 a 20 e retorne esse mesmo número, agora por extenso em string, mas 
# repita a solicitação se um número maior que 20 ou menor que zero for digitado

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 72' :^30}")
print('*' *30)

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    exibirNumero = int(input('Digite um número de 0 a 20'))
    if exibirNumero < 0 or exibirNumero > 20:
        print('Você digitou um número inválido')
    else:
        print(f'Você digitou {numeros[exibirNumero]}')
        break
    
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)