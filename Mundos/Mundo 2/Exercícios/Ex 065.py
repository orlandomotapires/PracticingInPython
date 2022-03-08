media = soma = count = perg = menor = maior = 0
while perg != 'N':
    n1 = int(input('Insira um valor: '))   
    if count == 0:
        maior = menor = n1           
    else: 
        if n1 > maior:
            maior = n1
        elif n1 < menor:
            menor = n1              
    count += 1
    soma += n1    
    perg = str(input("""Deseja continuar colocando valres ? 
    [S] Para continuar
    [N] Para fechar o programa
    Resposta: """)).upper().strip()[0]
media = soma / count
print('A media entre todos os valores digitas foi {}, O maior valor entre eles foi {} e O menor valor entre eles foi {}'. format(media, maior, menor)) 
   