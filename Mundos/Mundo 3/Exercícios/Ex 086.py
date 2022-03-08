matriz = list()
matriz2 = list()
lin = col = 0
for c in range(0, 9):
    matriz2.append(int(input(f'Insira um valor para [{lin}, {col}]: ')))
    
    matriz.append(matriz2[:])
    matriz2.clear()   
    col += 1
    if col == 3:
        lin += 1
        col = 0

print(matriz[0:3])       
print(matriz[3:6])
print(matriz[6:9]) 
    