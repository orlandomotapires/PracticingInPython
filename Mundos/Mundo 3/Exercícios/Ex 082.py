todos = []
pares = []
impares = []
num = 0
perg = 'S'
while perg != 'N':    
    num = int(input('Insira um número: '))    
    todos.append(num)
    if num%2 == 0:
        pares.append(num)
    else:
        impares.append(num)          
    perg = str(input('Deseja continuar ? [S/N]')).upper().strip()[0]
    while perg not in 'NS':
        print('Resposta invalida.', end = '')
        perg = str(input('Deseja continuar ? [S/N]')).upper().strip()[0]
todos.sort()
pares.sort()
impares.sort()
print('+=+' * 25, end = '')
print('  Fim do programa  ', end = '')
print('+=+' * 25)
print(f'A lista com todos os numeros é: {todos}')
print(f'A lista com os numeros pares é: {pares}')
print(f'A lista com os numeros impares é: {impares}')
