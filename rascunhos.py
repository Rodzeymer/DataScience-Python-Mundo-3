# desafio 90

turma = []
aluno = {}
contador = 0
while True:
    aluno['nome'] = str(input(f"Digite o nome do aluno: "))
    aluno['media'] = float(input(f"Digite a média de {aluno['nome']}: "))
    if aluno['media'] >=7:
        aluno['final'] = "Aprovado"
    else:
        aluno['final'] = "Reprovado"
    turma.append(aluno.copy())
    continuar = str(input("Quer continuar? S/N"))
    if continuar in 'Nn':
        break
for integrante in turma:
    print(f"O aluno {integrante['nome']} obteve média {integrante['media']} estando portanto {integrante['final']}.")

        