def linhas(mensagem):
    tamanho = len(mensagem)+4
    print('-'*tamanho)
    print(f"  {mensagem:^4}  ")
    print('-'*tamanho)
    
linhas('Mensagem1')
linhas('Mensagem bem longa para ver até onde vai essa bagaça')