# desafio 90

turma = []
aluno = {}

while True:
    aluno['nome'] = str(input(f"Digite o nome do aluno: "))
    aluno['media'] = float(input(f"Digite a média de {aluno['nome']}: "))
    if aluno['media'] >=6:
        aluno['final'] = "Aprovado"
    else:
        aluno['final'] = "Reprovado"
    turma.append(aluno.copy())
    print(f"O {aluno['nome']} obteve média {aluno['media']}, estando portanto {aluno['final']}")
    continuar = str(input("Quer continuar? S/N"))
    if continuar in 'Nn':
        break
for e in turma:
    for k, v in e.items():
        print(f"O campo {k} tem valor {v}")

        