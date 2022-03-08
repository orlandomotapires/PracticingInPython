valores = []
pos = 0
for c in range(0,5):
    valores.append(int(input(f'Insira um valor para a posicao {c}: ')))

print(f'A lista que voce acabou de criar é: {valores}')    
print(f'O maior valor digitado foi {max(valores)} e suas posições foram ', end = '')   
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i} ', end = '')
print('\n')
print(f'O menor valor digitado foi {min(valores)} e suas posições foram ', end = '')
for i, v in enumerate(valores):    
    if v == min(valores):
        print(f'{i} ', end = '')
