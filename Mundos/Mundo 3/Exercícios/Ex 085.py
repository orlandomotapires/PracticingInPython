listtot = list()
listimp = list()
listpar = list()
for c in range(0, 7):
    valor = int(input('Insira um valor: '))
    
    if valor%2 == 0:
        listpar.append(valor)
    else: 
        listimp.append(valor)
listpar.sort()
listimp.sort()
listtot.append(listpar[:])
listtot.append(listimp[:])


print('-=' * 30)
print(f'A lista completa é {listtot}')    
print(f'A lista so com os impares é {listimp}')
print(f'A list so com os pares é {listpar}')        