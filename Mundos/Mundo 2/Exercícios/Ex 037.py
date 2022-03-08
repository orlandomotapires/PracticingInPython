num = int(input('Digite um numero inteiro!!\n'))
base = int(input('Escolha a base de conversao, 1 para binario, 2 para octal e 3 para hexadecimal!\n'))
if base == 1:
   print('{} convertido para BINARIO é {}'. format(num, bin(num)[2:]))
    
elif base == 2:
    print('{} convertido para OCTAL é {}'. format(num, oct(num)[:2]))

elif base == 3:
    print('{} convertido para HEXADECIMAL é {}'. format(num, hex(num)[2:]))
else:
    print('Numero invalido, digite um valor correto!!!')