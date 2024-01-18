#rascunho 113


def leiaInt(numInteiro=0):
    inteiro=False
    try:
        while inteiro == False:
            i=str(input(numInteiro))
            if i.isdigit() == True:
                inteiro=True
                return i
            else:
                print('Erro: digite um valor inteiro')
    except KeyboardInterrupt:
        print(f"O usuário não informou os dados")
        
        
def leiaFloat(numDecimal=0):
    decimal=False
    try:
        while decimal == False:
            d=str(input(numDecimal))
            if d.isdigit() == True:
                decimal=True
                return d
            else:
                print('Erro: digite um valor real')
    except KeyboardInterrupt:
        print(f"O usuário não informou os dados")
        
def resultado(i, d):
    print(f"Você digitou inteiro: {i} e decimal: {d}")
    
i = leiaInt('Digite um Inteiro: ')
d = leiaFloat('Digite um Real: ')
resultado(i, d)