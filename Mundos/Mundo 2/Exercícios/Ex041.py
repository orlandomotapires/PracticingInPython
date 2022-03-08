nasc = int(input('Digite seu ano de nascimento\n'))
idade = 2021 - nasc
print(idade)
if idade <= 9:
    print('MIRIM')
elif (idade > 9) & (idade <= 14):
    print('INFANTIL')
elif (idade > 14) & (idade <= 20):  
    print('SÊNIOR')
elif idade > 20:
    print('MASTER')      
