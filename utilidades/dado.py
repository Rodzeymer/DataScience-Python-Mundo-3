#desafio 112 tentando

def leiaDinheiro(valor):
    if float(valor) == 'float':
        resumo(valor, incremento, decremento)
    else:
        print('ERRO!')
    
valor = input('Digite o valor: R$')
incremento = float(input('Digite o fator de incremento'))
decremento = float(input('Digite o fator de decremento'))

leiaDinheiro(valor)