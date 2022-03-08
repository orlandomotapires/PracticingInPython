valorcasa = float(input('Digite o valor da casa\n'))
salario = float(input('Digite o salario do comprador\n'))
anos = int(input('Em quantos anos você vai pagar ?\n'))
meses = anos * 12
prestacao = valorcasa/meses
valormax = salario * 0.3
if prestacao > valormax:
    print('Seu emprestimo foi RECUSADO!!!\n')   
else:
    print('Seu imprestimo foi aceito!!!\n')     

print('valormax = {} '. format(valormax))
print('prestacao = {}'. format(prestacao))
print('meses = {} '. format(meses))