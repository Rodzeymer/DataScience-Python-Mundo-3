# Esse desafio fia mais simples que o anterior, agora fiz um algoritmo que leia quantos
# algarismos o susário queira e os insere numa lista, ao final deve exibir na tela quantos 
# números foram digitados, quais foram esses números em ordem decrescente e se o 5 faz ou não
# parte dessa lista

# Começamos com um loop e dentro dele pedimos os números e se o usuário quer inserir novos 
# números, após a quebra do loop analisamos a lista, para saber quantos números ela contém, que 
# será nossa quantidade de números, depois organizamos a lista e a invertemos, para obter a 
# lista em ordem decrescente e verificamos se há ou não o número 5 dentre seus componentes e 
# exibimos mensagens na tela com os resultados dessas análises.

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 81' :^30}")
print('*' *30)
lista = []

while True:
    novoNumero = int(input('Digite um novo número'))
    lista.append(novoNumero)
    continuar = input('Quer continuar? [S/N]').lower()
    if continuar == 'n':
        break
print(f'Foram digitados {len(lista)} números')
lista.sort()
lista.reverse()
print(f'A lista em ordem decrescente é {lista}')
if 5 in lista:
    print('O 5 foi digitado ao menos uma vez')
else:
    print('O número 5 não foi digitado')

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)