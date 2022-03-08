frase = str(input('Digite uma frase!\n'))
frasemin = frase.lower()
fraseinv = frasemin[::-1]
if fraseinv == frasemin:
    print('É palindromo')
else:
    print('Não é palindromo')    