numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    exibirNumero = int(input('Digite um número de 0 a 20'))
    if exibirNumero < 0 or exibirNumero >20:
        print('Você digitou um número inválido')
    else:
        print(f'Você digitou {numeros[exibirNumero]}')
        break