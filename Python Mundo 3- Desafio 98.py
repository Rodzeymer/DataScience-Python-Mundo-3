# Nesse desafio foi preciso dar uma leve pesquisada sobre o laço for pra fazer o contador
# inverso, ou contador regressivo, mas foi bem simples de implementar

# Esse algoritmo deve fazer duas contagens automáticas, de 1 até 10, com o passo de 1 em 1, e 
# de 10 até 0 recuando de 2 em 2. Depois o sistema pede para o usuário informar o início e fim
# da contagem e o passo da contagem, imprimindo a contagem ao final, com o comando time.sleep 
# para deixar a experiência mais amigável.

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 98' :^30}")
print('*' *30)

import time

def contador1():
    print("Contador 1:")
    print('Contando de 1 até 10, de 1 em 1')
    for digito in range(1, 11, 1):
        print(f"{digito} ", end='')
        time.sleep(0.3)
    print()
    print('-'*30)
    time.sleep(0.6)

def contador2():
    print("Contador 2:")
    print('Contando de 10 até 0, recuando de 2 em 2')
    for digito in range(10, -2, -2):
        print(f"{digito} ", end='')
        time.sleep(0.3)
    print()
    print('-'*30)
    time.sleep(0.6)
    
def personalizado(inicio, fim, passo):
    print('Contador Personalizado')
    for digito in range(inicio, fim, passo):
        print(f"{digito} ", end='')
        time.sleep(0.3)
    print()
    print('-'*30)
    
contador1()
contador2()

inicio = int(input('Digite o início da contagem'))
fim = int(input('Digite o fim da contagem'))
passo = int(input('Digite o passo da contagem, número negativo para contagem inversa'))

personalizado(inicio, fim, passo)

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)