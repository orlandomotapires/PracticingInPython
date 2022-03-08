n1 = float(input('Digite a primeira nota do aluno!\n'))
n2 = float(input('Digite a segunda nota do aluno!\n'))

media = (n1 + n2) / 2
print(media)
if media < 5:
    print('REPROVADO')
elif (media >= 5) & (media <= 6.9):
    print('RECUPERAÇÃO')
else:
    print('APROVADO')     
