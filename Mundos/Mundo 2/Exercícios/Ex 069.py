pm = h = mm = perg = 0
while perg != 'N':
    
    idade = int(input('Digite sua idade: '))
    while idade < 0:
        print('Insira um valor válido!')
        idade = int(input('Digite sua idade: '))
    
    sexo = str(input('Insira seu sexo, [M][F] ')).upper().strip()[0]    
    while ( sexo != 'M') & ( sexo != 'F'):
        print('Insira um valor válido!')
        sexo = str(input('Insira seu sexo, [M][F] ')).upper().strip()[0] 
    
    perg = str(input('Deseja continuar cadastrando pessoas ? [N][S]\n')).upper().strip()[0] 
    while ( perg != 'S') & ( perg != 'N'):
        print('Insira um valor válido!')
        perg = str(input('Deseja continuar cadastrando pessoas ? [N][S]\n')).upper().strip()[0] 
    print(perg)
    if sexo == 'M':
        h += 1
    
    if idade > 18:
        pm += 1

    elif (sexo == 'F') and (idade < 20):
        mm += 1     

print(f""" 
{pm} pessoas tem mais de 18
{h} homens foram cadastrados
{mm} mulheres tem menos de 20 anos""")          