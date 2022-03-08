op = 0
tabela = ('Palmeiras', 'Atletico - MG', 'Fortaleza', 'Bragantino', 'Athletico - PR', 'Flamengo', 'Ceará SC', 'Bahia', 'Fluminense', 'Santos', 'Atlético - GO', 'Corinthians', 'Internacional', 'Juventude', 'São Paulo', 'América - MG', 'Cuiabá', 'Sport Recife', 'Grêmio', 'Chapecoense')
while True:
    print(""" 
SELECIONE A OPCAO ABAIXO PARA CADA FUNCIONALIDADE
[1] 5 PRIMEIROS COLOCADOS
[2] 4 ULTIMOS COLOCADOS
[3] TIMES EM ORDEM ALFABETICA
[4] POSICAO DO TIME CHAPECOENSE""")
    op = int(input('Insira a opcao desejada: '))

    if op < 0 | op > 4:
        print('Insira um valor válido')
        op = int(input('Insira a opcao desejada: '))

    if op == 1:
        print(tabela[:5])
    elif op == 2:
        print(tabela[16:])
    elif op == 3:
        print(sorted(tabela))
    elif op == 4:
        print(tabela.index('Chapecoense')+1)  
    elif op == 0:
        break     
