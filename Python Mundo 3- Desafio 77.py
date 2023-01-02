lista = ('Brasil', 'Russia', 'India', 'China', 'South Africa')

for palavra in lista:
    vogais = []
    tupla = tuple(palavra)
    for letra in range (0, len(tupla)):
        if tupla[letra] in 'AaEeIiOoUu':
            vogais.append(tupla[letra])
    print(f'Na palavra {palavra} há as vogais{vogais}')