n1 = float(input('Insira o primeiro número\n'))
n2 = float(input('Insira o segundo número\n'))
n3 = float(input('Insira o terceiro número\n'))
max = n1
if n2 > max:
    max = n2
if n3 > max:
    max = n3

print('O maior numero entre os 3 é {}'. format(max))       