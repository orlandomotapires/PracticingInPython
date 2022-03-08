listagem = ('Compiuter', 1000.50, 'Borracha', 2.25, 'Caderno', 5.10, 'Transferidor', 9.12 )
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R$ {listagem[pos]:>7.2f}')    