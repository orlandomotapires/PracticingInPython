import random
n1 = str(input('Nome do primeiro aluno\n'))
n2 = str(input('Nome do segundo aluno\n'))
n3 = str(input('Nome do terceiro aluno\n'))
n4 = str(input('Nome do quarto aluno\n'))
n5 = str(input('Nome do quinto aluno\n'))
lista = [n1,n2,n3,n4,n5]
random.shuffle(lista)
print(lista)