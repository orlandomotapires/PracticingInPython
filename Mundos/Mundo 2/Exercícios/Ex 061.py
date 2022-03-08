num = int(input('Digite um numero inteiro!\n'))
raz = int(input('Digite a razao da sua PA!\n'))
c = res = pos = 0
while pos != 10:
    res = num * raz * pos 
    pos += 1   
    print(res)