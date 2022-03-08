from ast import Str
soma = prod1k = nprodbarat = c = vprodbarat = perg = 0
while perg != 'N':
    
    nome = str(input('Digite o nome do produto: '))
   
    preco = float(input('Insira o preco do produto: '))
    while preco < 0:
        print('Insira um valor válido!')
        preco = float(input('Insira o preco do produto: '))
    
    perg = str(input('Deseja continuar? [S/N]')).upper()
    while (perg != 'S') and (perg != 'N'):
        print('Insira um valor válido')
        perg = str(input('Deseja continuar? [S/N]')).upper()   
    soma += preco
    if preco > 1000:
        prod1k += 1

    if c == 0 or c > 0:        
        vprodbarat = preco
        nprodbarat = nome    
    c += 1        
print('--------RESULTADOS DA COMPRA--------')
print(f"""
O total gasto nesta compra foi:  R${soma:.2f} 
Quantidade de produtos que custam mais de R$1000 foi de {prod1k} produtos
O nome do produto mais barato comprado é {nprodbarat} e o preço dele é R${vprodbarat:.2f}""")            
