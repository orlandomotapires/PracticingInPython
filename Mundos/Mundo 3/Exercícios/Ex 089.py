lista = list()
perg = 'S'
media = num = nota1 = nota2 = nome = 0  
while perg not in 'N':
    nome = str(input('Insira o nome do aluno: '))
    nota1 = int(input('Insira a primeira nota do aluno: '))
    nota2 = int(input('Insira a segunda nota do aluno: ')) 
    media = (nota1 + nota2) / 2       
    perg = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    lista.append([nome, [nota1, nota2], media])
    while perg not in 'SN':
        print('Resposta inválida! Tente novamente.')
        perg = str(input('Deseja continuar? [S/N]')).upper().strip()[0]          
print('-='* 25 ,'BOLETIM FINAL!', '-='* 25)
print(f'{"No.":<4} {"NOME":<10} {"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(lista):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8.1f}')    
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        break
    if opc  <= len(lista) - 1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')  