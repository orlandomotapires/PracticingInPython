nasc = int(input('Informe o seu ano de nascimento!\n'))
idade = 2021 - nasc

print('Sua idade é {}'. format(idade))
if idade < 18:
    falta = 18 - idade
    print('Ta safe papito você esta abaixo dos 18 anos!')
    print('Faltam {} anos para você se alistar!'. format(falta))
elif idade == 18:
    print('Tem que se alistar einnnn!\n')
elif idade > 18:
    oh = idade - 18
    print('Ja passou da hora ein!')   
    print('Já tem {} anos que você esta atrasado quanto ao alistamento!'. format(oh))

