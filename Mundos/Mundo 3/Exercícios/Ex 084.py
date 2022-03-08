lista = list()
dado = list()
pessoasleves = list()
pessoaspesadas = list()
perg = 'S'
totpes = leve = pesado = 0
while perg not in 'Nn':
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: '))) 

    if totpes == 0:
        leve = pesado = dado[1]

    else:
        if dado[1] >= pesado:
            pesado = dado[1]
            pessoaspesadas.append(dado[0])
        elif dado[1] <= leve:
            leve = dado[1]
            pessoasleves.append(dado[0])
    perg = str(input('Deseja continuar? [S/N]')).strip().upper()[0]    
    while perg not in 'SN':
        print('Resposta invalida!')
        perg = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    
    lista.append(dado[:])
    dado.clear()
    totpes += 1

    


print('-=' * 30)
print(f'Ao todo, foram cadastradas {totpes} pessoas')
print(f'O maior peso foi de {pesado}Kg. Peso de ', end = '')
for p in lista:
     if p [1] == pesado:
         print(p[0], end = ' ')
print()
print(f'O menor peso foi de {leve}Kg. Peso de ', end = '')
for p in lista:
    if p[1] == leve:
        print(p[0], end = ' ')