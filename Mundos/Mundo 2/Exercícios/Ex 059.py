op = 85  

v1 = float(input('Digite um valor: '))
v2 = float(input('Digite outro valor: '))

while op != 5:    
    op = int(input("""Qual das operações abaixo você deseja executar entre os dois numeros escolhidos ?
    [1] SOMA
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA
    Operação escolhida:  """))

    #VARIAVEIS
    soma = 0
    multiplicar = 0
    maior = 0
    novosnum = 0
    sair = 0

    if op == 1:
        soma = v1 + v2
        print('A soma entre {} e {} é: {}'. format(v1,v2,soma))
    elif op == 2:
        multiplicar = v1 * v2
        print('A multiplicação entre {} e {} é: {}'. format(v1,v2,multiplicar))
    elif op == 3:
        if v1 > v2:
            maior = v1 
            print('O maior número entre {} e {} é: {}'. format(v1,v2,maior))       
        elif v2 > v1:
            maior = v2  
            print('O maior número entre {} e {} é: {}'. format(v1,v2,maior))  
    elif op == 4:
        v1 = float(input('Digite um valor: '))
        v2 = float(input('Digite outro valor: '))
    elif op == 5: 
        print('Zzzzzzzz')
    
    else: 
        print('Insira um valor válido!')    
print('Obrigado por usar meus seviços. Volte sempre e tenha um bom dia!!!')            