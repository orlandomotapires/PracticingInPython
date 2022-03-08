media = 0
somaidade = 0
maioridadehomem = 0
nomevelho = ''
nummulher = 0

for c in range(1,5):
    print('...........  {} PESSOA  ...........'.format(c))
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm' :
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome 
    if idade < 20 and sexo in 'Ff' :
        nummulher += 1

mediaidade = somaidade/4   
print('A media de idade do grupo é {}'. format(mediaidade))
print('O homem mais velho tem {} anos e se chama {} '. format(maioridadehomem, nomevelho))
print('{} mulheres tem menos de 20 anos'.format(nummulher))