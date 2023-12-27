alunos = []

while True:
    alunoNome = str(input(f"Digite o nome do aluno"))
    nota1 = float(input(f"Digite a primeira nota de {alunoNome}"))
    nota2 = float(input(f"Digite a segunda nota nota de {alunoNome}"))
    media = (nota1+nota2)/2
    alunos.append([alunoNome, [nota1, nota2], media])
    print(alunos[0])
    continuar = str(input(f"Quer continuar?"))
    if continuar in 'Nn':
        break
