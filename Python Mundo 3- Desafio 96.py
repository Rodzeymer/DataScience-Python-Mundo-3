# Começando a parte de funções em Python, temos que é bem simples, com a palavra reservada 'def'
# passamos instruções, podendo conter todo tipo de estrutura, loops, condicionais, listas, 
# tuplas, dicionários, o que for, e chamar a função sempre que necessário, para economizar
# código, memória e processamento, reduzindo a complexidade dos algoritmos e facilitando sua
# leitura, manutenção e reusabilidade.

# O algoritmo, bem simples, pede largura e comprimento do usuário e devolve a área calculada, 
# bem simples, mas funcional.

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 96' :^30}")
print('*' *30)

def area(largura, comprimento):
    terreno = largura*comprimento
    print(f"Com largura de {largura} m e comprimento de {comprimento} m, temos que sua área é de {terreno} m²")


largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))

area(largura, comprimento)

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)