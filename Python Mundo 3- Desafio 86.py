# Esse desafio foi dificil, por vezes tentando cheguei perto da solução, mas a parte de formatação, 
# me enganava e eu achava que não era assim, que teria uma forma mais prática de se fazer, mas no final
# era assim mesmo

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 86' :^30}")
print('*' *30)

matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um valor para o endereço {l}, {c}"))
print('*' *30)
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end='')
    print()
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)