num1 = int(input('Digite um numero inteiro!\n'))
num2 = int(input('Digite outro numero inteiro!\n'))

if num1 > num2:
    print('{} é maior que {}, sendo assim {} é o maior numero dentre eles!\n'. format(num1, num2, num1))
elif num2 > num1:
    print('{} é maior que {}, sendo assim {} é o maior numero dentre eles!\n'. format(num2, num1, num2)) 
else:
    print('Não há um numero maior entre eles, pois {} e {} sao iguais'. format(num1, num2))       