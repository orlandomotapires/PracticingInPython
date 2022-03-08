from datetime import date
anoatual = date.today().year
p = 0
for c in range(0,7):
    nasc = int(input('Digite sua data de nascimento!\n'))
    n1 = anoatual - nasc
    if n1 >= 18:
        p += 1
print('{} pessoas atingiram a maioridade!\n'. format(p))        