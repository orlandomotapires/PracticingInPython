matriz = list()
matriz2 = list()
lin = col = totpar = totimpar = somaterc = maiorseg = 0
for c in range(0, 9):
    matriz2.append(int(input(f'Insira um valor para [{lin}, {col}]: ')))  
    
    if matriz2[0]%2 == 0:
        totpar += matriz2[0]
    else:
        totimpar += matriz2[0]    
   
    if col == 2:
        somaterc += matriz2[0]    

    col += 1
    
    if col == 3:
        lin += 1
        col = 0  

    matriz.append(matriz2[:])
    matriz2.clear() 
print('-=' * 30)
print('A matriz final foi: ')
print(matriz[0:3])       
print(matriz[3:6])
print(matriz[6:9]) 
print(f'A soma de todos os valores pares digitados foi: {totpar}')
print(f'A soma de todos os valores impares digitados foi: {totimpar}')
print(f'O maior valor da segunda linha foi: {max(matriz[3:6])}')
print(f'A soma dos valore da terceira coluna resultou em: {somaterc}')