salario = float(input('Insira o seu salario\n'))
if salario > 1250.00:
    novosalario = salario * 1.10
else:
    novosalario = salario * 1.15

aumento = novosalario - salario 
print('O aumento foi de: {:2f}'. format(aumento))
print('O salario antigo era: {:2f} e o salario novo é: {:2f}.'.format(salario,novosalario))        