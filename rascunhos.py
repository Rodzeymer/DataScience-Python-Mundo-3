# Rascunho do 108

# moeda.py

import locale
loc = locale.getlocale()
locale.setlocale(locale.LC_NUMERIC, "pt_BR")

def aumentar(valor, fator):
    valorAumentado = valor*fator
    return round(valorAumentado, 2)

def diminuir(valor, fator):
    valorReduzido = valor-(valor*fator)
    return round(valorReduzido, 2)
    
def dobro(valor):
    valorDobrado = valor*2
    return round(valorDobrado, 2)

def metade(valor):
    valorMetade = valor/2
    return round(valorMetade, 2)
    
def moeda(valor):
    emReal = str(f"R${valor:,.2f}")
    return emReal

valor = float(input('Digite o valor: R$'))

print(f"O valor {valor} agora é {moeda(valor)}")
print(f"O valor {moeda(valor)} aumentado em 10% é {moeda(aumentar(valor, 1.1))}")
print(f"O valor {moeda(valor)} reduzido em 13% é {moeda(diminuir(valor, 0.13))}")
print(f"O valor {moeda(valor)} dobrado é {moeda(dobro(valor))}")
print(f"O valor {moeda(valor)} pela metade é {moeda(metade(valor))}")

