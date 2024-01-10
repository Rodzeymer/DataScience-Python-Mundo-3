# Esse desafio foi fácil, deu um certo trabalho alinhar o texto direito, mas com um artifício
# técnico ficou tudo certo

# Mais um algoritmo simples, ele pega uma mensagem informada pelo usuário e a imprime com 
# linhas acima e abaixo da mensagem e o texto da mensagem centralizado nessas linhas, até que
# decida encerrar o programa

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 97' :^30}")
print('*' *30)

def linhas(mensagem):
    tamanho = len(mensagem)+4
    print('-'*tamanho)
    print(f"  {mensagem}  ")
    print('-'*tamanho)
    
    
while True:
    mensagem = str(input("Digite uma mensagem para imprimir, 'sair' encerra."))
    if mensagem.upper() in 'SAIR':
        break
    else:
        linhas(mensagem)

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)