num = int(input('Digite um numero inteiro!\n'))
mult = 0
for c in range(2,num):       
    if num % c == 0:
        print('Multiplo de {}'. format(c))
        mult += 1


if mult == 0:
    print('É primo')
else:
    print('Não é primo')    
