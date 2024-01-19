# Esse desafio foi dificil pois a biblioteca estava dificil de acessar, pois outras bibliotecas 
# foram desativadas para que os comandos fossem centralizados em uma nova lib. Mas feito o 
# comando de pedido de acesso o uso dele em um tratamento de erro foi simples.


# Neste desafio foi preciso criar um código que faça o acesso a um site na internet, indique se
# o acesso foi realizado por meio de uma string e através de um tratamento de exceção, caso 
# ocorra falha para colocar uma mensagem de erro personalizada, agora pode-se verificar o acesso
# de qualquer site, nesse desafio foi usada a página do pudim.com.br, uma icônica página que foi
# construída à muito tempo, não se sabe por quem, que mostra a foto de um pudim, simplesmente.

print('*' *30)
print(f"{'Python Mundo 3 - Desafio 114' :^30}")
print('*' *30)

import urllib
import urllib.request 

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print(f"Não consegui acessa o {'pudim.com.br'}")
else:
    print(f"O site {'pudim.com.br'} foi acessado com sucesso")
    print(site.read())

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)