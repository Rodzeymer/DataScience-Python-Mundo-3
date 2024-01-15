# Esse algoritmo reúne tudo que foi estudao até então, a função, doc string, parâmetros 
# flexíveis e parâmetros opcionais, como os dicionários e suas manupulações

# Neste algoritmo o sistema pega as informações inseridas e as joga dentro da função, que irá 
# cálculos de mínimos e máximos, média e situação do aluno cadastrado, além da situação dele
# peranto a média, e ao final exibe as informações do dicionário, sendo a situação um parâmtro
# opicional, e quando não solicitado não é impresso.


print('*' *30)
print(f"{'Python Mundo 3 - Desafio 105' :^30}")
print('*' *30)


def medias(*notas, mostrar = False):
    """A função pega os dados informados na linha 30 e os coloca dentro da função, 
        calculando quantas notas foram inseridas, as notas máxima e mínima, a sua média e
        se o usuário quiser a situação do aluno.
        :notas: as notas do aluno
        :mostrar: se o usuário quer exibir a situação final do aluno
        :return: o dicionário onde estão as informações de quantidade de notas, qual foi a nota 
            mínima e máxima, a média e se solicitado a situação do aluno perante a média.
    """
    Cadastro={}
    soma= 0
    c = 0
    Cadastro['Total'] = len(notas)
    for c in range (0, Cadastro['Total']):
        if c == 0:
            Cadastro['Menor'] = notas[c]
            Cadastro['Maior'] = notas[c]            
        else:
            if Cadastro['Menor']> notas[c]:
                Cadastro['Menor']=notas[c]
            if notas[c] > Cadastro['Maior']:
                Cadastro['Maior'] = notas[c]
        soma = notas[c] + soma
        mediaTotal = soma/Cadastro['Total']
        Cadastro['Média'] = round(mediaTotal,2)
    if mostrar == True:
        if Cadastro['Média'] >=7:
            Cadastro['Situação'] = "Aprovado!"
        if Cadastro['Média'] >=6 and Cadastro['Média'] <7:
            Cadastro['Situação'] = "Razoável, ainda dá para ser aprovado"
        if Cadastro['Média'] <6:
            Cadastro['Situação'] = "REPROVADO"
        print(Cadastro) 
    else:
        print(Cadastro)

medias(9,6,5, mostrar = True)

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)  