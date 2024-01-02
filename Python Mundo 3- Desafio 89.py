# Esse desafio foi bem dificil, mas pensando um pouco e estruturando o "banco de dados" dá pra fazer
# de maneira bem interessante e simples, apesar de não ser fácil em um primeiro momento.

# Inicial o algoritmo inicia a lista vazia de alunos, e depois percorre o primeiro loop solicitando ao 
# usuário o nome e as duas notas de cada aluno, solicitando a confirmação de continuar, para executar o
# loop novamente e cadastrar um novo aluno, até que o usuário decida encerrar essa funcionalidade.
# Ao final o programa exibe uma enumeração de todos os cadastrados na lista, com nome e média, e pergunta
# ao usuário se ele deseja acessar o registro de algum aluno, para saber da notas, que não são exibidas 
# ainda. O usuário pode abrir todos os registros, um a um, e para encerrar a aplicação basta digitar 999
# que o programa interrompe a execução apresentando mensagens de encerramento e de agradecimentos.

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 89' :^30}")
print('*' *30)

alunos = []

while True:
    alunoNome = str(input(f"Digite o nome do aluno"))
    nota1 = float(input(f"Digite a primeira nota de {alunoNome}"))
    nota2 = float(input(f"Digite a segunda nota nota de {alunoNome}"))
    media = (nota1+nota2)/2
    alunos.append([alunoNome, [nota1, nota2], media])
    continuar = str(input(f"Quer continuar?"))
    if continuar in 'Nn':
        break
print(f"{'No.':<4}{'NOME':<10}{'MÉDIA':>8}")
print("-"*26)
for i, a in enumerate(alunos):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")

while True:
    print('-'*30)
    numero = int(input('Deseja exibir notas de qual aluno (No.) (999 encerra)'))
    if numero == 999:
        print('ENCERRANDO APLICAÇÃO')
        break
    if numero <= len(alunos) -1:
        print(f"Notas de {alunos[numero][0]} são {alunos[numero][1]}")
print("OBRIGADO PELA PREFERÊNCIA!")

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)