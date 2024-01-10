# Agora foi fazer um analisador de maior número, como a função pega os números e os colocam em
# uma tupla foi preciso revisar os comandos de tuplas, ajeitar algumas coisas, mas o algoritmo
# saiu como esperdao.

# Esse programa pega números já informados, tuplas de diversos tamanhos, analisa a quantidade de
# números informados e mostra o maior informado pelo sistema, se não for informado nenhum 
# valor ele informa que zero números foram informados e não há maior número.

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 99' :^30}")
print('*' *30)

import time

def maior(*numeros):
    print('-='*30)
    print('Analisando os valores informados...')
    time.sleep(0.6)
    if len(numeros)<1:
        time.sleep(0.3)
        print(f"Foram informados {len(numeros)} números ao todo.")
        print(f"O maior valor informado foi .")
    else:
        for c in range(0, len(numeros)):
            print(f"{numeros[c]} ", end='')
            time.sleep(0.3)
        print(f"Foram informados {len(numeros)} números ao todo.")
        time.sleep(0.3)
        maior = max(numeros)
        print(f"O maior valor informado foi {maior}.")
        time.sleep(0.3)
    
maior(9, 34, 10, 3)
maior(3, 99, 87, 45, 109)
maior(6)
maior()

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)