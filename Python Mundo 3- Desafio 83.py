# Depois de muito quebrar a cabeça 'furtei' a solução do Guanabara, estava quase chegando lá
# mas o professor foi mais elegante e assertivo na resposta. Neste algoritmo o usuário irá 
# digitar uma expressão algébrica qualquer e o programa deverá conferir se, existindo 
# parênteses se eles estão corretamente utilizados, sempre o simbolo que abre aparecendo antes
# do que fecha e nunca depois dele e se todos os parênteses abertos estão fechados.

# Então o sistema pede a expressão ao usuário, armazenando-a em uma variável do tipo string e 
# cria uma lista, onde serão armazenados os parênteses encontrados. Então percorre toda a 
# expressão testando cada símbolo e armazenando os parênteses abertos na pilha e removendo-os
# a cada fechamento encontrado, se encontrar um fechamento e a pilha não contiver nenhuma 
# abertura ele adiciona o fechamento. Ao final é testado se a pilha está zerada, ou seja, toda
# abertura teve seu respectivo fechamento, ou se contiver um abre parenteses ou um fecha 
# parenteses na pilha, significa que sobrou algum parenteses a mais.

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 83' :^30}")
print('*' *30)

expressao = str(input('Digite a expressão a ser analisada'))
pilha = []
for simbolo in expressao:
    if simbolo =='(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) >0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print(f'A expressão "{expressao}" é válida')
else:
    print(f'A expressão "{expressao}" é inválida')

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)