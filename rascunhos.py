# desafio 102

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
        