count =  soma =  n1 = 0
while n1 != 999:
    n1 = int(input('Insira um número: '))
    count += 1
    soma += n1
    
    if n1 == 999:
        soma -= 999
        count -= 1
print('Foram inseridos {} valores e a soma entre eles vale {}'. format(count, soma))