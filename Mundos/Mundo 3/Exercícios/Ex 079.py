pos = n = 0
valores = []
while True:
        n = (int(input(f'Insira o valor na posição {pos}: ')))
        if n not in valores:
            valores.append(n)
            print('Valor adicionado com sucesso')
        else:
            print('Valor duplicado, nao vou adicionar')   
        perg = str(input('(Insira S para continuar ou insira N para parar o programa) ')).upper().strip()[0]              
        if 'N' in perg:
            break
        pos += 1
valores.sort()  
print('-_-_-' * 3) 
print('Fim do programa')  
print('-_-_-' * 3)
print(f'Aqui esta, em ordem crescente, a lista que voce digitou {valores}!')     