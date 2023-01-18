# WIP pq aceita expressão como 9)(9 como válida

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 83' :^30}")
print('*' *30)

expressao = input('Digite a expressão a ser analisada')

if "(" in expressao or ")" in expressao:
    parentesesAbertos = expressao.count('(')
    parentesesFechados = expressao.count(')')
    if parentesesAbertos != parentesesFechados or expressao.startswith(")") or expressao.endswith("("):
        print('Segundo minha análise, a expressão analisada apresenta inconsistências')
    elif parentesesAbertos == parentesesFechados:
        print('A expressão apresentada é válida, segundo minha análise!')
else:
    print('A expressão inserida não apresenta parênteses, logo não há possibilidades de erros')

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)