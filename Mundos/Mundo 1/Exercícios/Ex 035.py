l1 = float(input('Insira o primeiro lado do triangulo\n'))
l2 = float(input('Insira o segundo lado do triangulo\n'))
l3 = float(input('Insira o terceiro lado do triangulo\n'))

if (l1 + l2 > l3) & (l2 + l3 > l1) & (l1 + l3 > l2):
    print('Da pra dale pain!!!')
else:
    print('Nao da pra fazer um triangulo')