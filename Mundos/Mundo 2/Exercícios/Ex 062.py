num = int(input('Digite um numero inteiro!\n'))
raz = int(input('Digite a razao da sua PA!\n'))
c = res = pos = perg = 0
fim = 10
perg2 = 25
while (perg2 != 0) & (perg != 'N'):
    while pos < fim:
        res = num + raz * pos
        pos += 1   
        print(res)    
    
    perg = str(input('Deseja continuar calculando a progressao aritimetica? Digite S para continuar e N para parar:\n')).upper()        
    if perg == 'S':
        perg2 = int(input('Quantos mais numeros voce deseja acrescentar a PA?\n'))
        fim += perg2
print('Foram mostrados {} termos!'. format(fim))