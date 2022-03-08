valores = []
perg = 'S'
while perg != 'N':
    valores.append(int(input('Insira um valor: ')))
    perg = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
valores.sort(reverse=True)
print(f'Foram digitados {len(valores)} valores')
print(f'Aqui está a lista ordenada de forma decrescente {valores}')
if 5 in valores[:]:
    print(f'O valor 5 foi digitado e esta na posicao {valores.index(5)}')
else:
    print('O valor 5 nao foi digitado')    