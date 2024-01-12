# Usando parâmetros opcionais pode-se criar uma função que pode ou não receber um parâmetro e
# vai continuar funcionando, o mais dificil nesse caso foi de saber quando colocar a parte que 
# imprime o processo passo a passo na tela.

# Este algoritmo recebe um número do usuário e calcula sua fatoração, o usuário ainda escolhe 
# imprimir ou não o processo de cálculo, ao final o cálculo é realizado, mostrando ou não o
# resultado.

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 102' :^30}")
print('*' *30)

from time import sleep

def fatorial(numero = 1, show='N'):
    f=1
    for c in range(numero, 0, -1):
        f*=c
        sleep(0.5)
        if show == 'S':
            print(f"{c} ", end='')
            if c > 1:
                print("x ", end='')
            if c == 1:
                print(f"= {f}")
                sleep(0.5)
    if show == 'N':
        print(f"{numero}! = {f}")
numero = int(input('Digite um número a ser calculado seu fatorial'))
show = str(input('Quer ver o processo? [S/N]')).upper()

fatorial(numero, show)

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)  