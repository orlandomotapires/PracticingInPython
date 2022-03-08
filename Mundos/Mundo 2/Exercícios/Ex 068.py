from random import randint

eu = acao = real = soma = c = v = 0
while acao == real:
    comp = randint(0,10)
    print(comp)
    acao = str(input('Escolha se voce quer par [P] ou impar [I]: ')).upper().strip()[0]
    eu = int(input('Insira um valor de 1 a 10 para o par ou impar: '))
    c += 1
    soma = eu + comp
    
    if soma % 2 == 0:
        print('O resultado do par ou impar foi PAR!')
        real = 'P'

    elif soma % 2 != 0:
        print('O resultado do par ou impar foi IMPAR!')    
        real = 'I'
    
    if acao != real:
        print('VOCE PERDEU !!!')

    if acao == real:
        print(f'VOCE VENCEU A RODADA, o computador escolheu {comp} e voce escolheu {eu}, soma resultou em {soma} ')
        v += 1  

print(f'Voce tentou {c} vezes e ganhou {v} vezes consecutivas!!!')        
print(comp)        