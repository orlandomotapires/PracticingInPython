d = dict()
lista = list()
soma = 0
while True:
    d.clear()
    d['nome'] = str(input('Nome: ')).strip()   
    d['sexo'] = str(input('Sexo: ')).strip().upper()[0]
    while d['sexo'] not in 'MF':
        print('Resposta Inválida, tente novamente!')
        d['sexo'] = str(input('Sexo: ')).strip().upper()[0]  
    d['idade'] = int(input('Idade: '))   
    while d['idade'] < 0:
        print('Resposta Inválida, tente novamente!')
        d['idade'] = int(input('Idade: '))      
    perg = str(input('Deseja continuar cadastrando ? [S/N]')).strip().upper()[0]
    while perg not in 'SN':
        print('Resposta Inválida, tente novamente!')
        perg = str(input('Deseja continuar cadastrando ? [S/N]')).strip().upper()[0]    
    lista.append(d.copy())        
    soma += d['idade']       
    if perg in 'N':
        break   
print(lista)      
print('-='*30)
print(f'Foram cadastradas {len(lista)} pessoas') 
print(f'A média de idade do grupo é: {soma/len(lista):5.2f}')
print('Mulheres: ', end = '')
for e in lista:
    if e['sexo'] in 'F':
        print(f'{e["nome"]} ', end = '')
print()  
print('Lista de pessoas que estao acima da média: ')     
for p in lista:
    if p['idade'] >= soma/len(lista):
        print('     ', end = '')
        for k, v in p.items():
            print(f'{k} = {v}; ', end = '')
        print()
print(' <<<<<<<< ENCERRADO >>>>>>>> ')            
