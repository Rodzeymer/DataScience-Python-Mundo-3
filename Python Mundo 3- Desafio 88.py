# Esse desafio é um clássico, muito bom. Foi até divertido fazer, lembrar de alguns fundamentos e
# funcionalidades e pesquisar um pouco.
# Nesse algoritmo o usuário irá informar quantas apostas de loteria, com 6 dezenas entre 1 e 60, sem 
# repetições, o usuário quer fazer. Então o sistema determina primeiro a lista de dezenas disponíveis e 
# as coloca em uma lista, com elementos de 1 a 60, depois sorteia, com o random.sample, n números de 
# apostas com 6 dezenas, que não se repetem no mesmo jogo, mas que pode se repetir entre jogos, imprimindo
# os resultados na tela com intervalo de 1.5 segundo, ficando mais agrádavel ao usuário ler as apostas 

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 88' :^30}")
print('*' *30)

import random
import time

alternativas =[]
for alternativa in range(1,60):
    alternativas.append(alternativa)
    alternativa = alternativa+1

palpites = int(input(f"Serão feitos quantos palpites de 6 dezenas?"))
for quantidade in range (0, palpites):
    dezena = random.sample(alternativas, 6)
    dezena.sort()
    print(f"A aposta {quantidade+1} será : {dezena} ")
    time.sleep(1.5)

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)