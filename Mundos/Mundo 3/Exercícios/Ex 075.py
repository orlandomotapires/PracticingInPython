n1 = (int(input('Insira o primeiro valor: ')), int(input('Insira o segundo valor: ')), int(input('Insira o terceiro valor: ')), int(input('Insira o quarto valor: ')))
          
print('-_-_-' * 20)
print(f'A tupla completa é {n1}')
print('-_-_-' * 20)

if n1.count(9) > 0: 
    print(f'Apareceu 9 {n1.count(9)} vezes')

if n1.count(9) == 0:
    print('-_-_-' * 20)
    print('O valor 9 nao foi digitado!')  
    print('-_-_-' * 20)

if n1.count(3) > 0:
    print(f'O primeiro valor 3 foi digitado na posição {n1.index(3)+1}')

if n1.count(3) == 0:
    print('-_-_-' * 20)
    print(f'O valor 3 nao foi digitado!')
    print('-_-_-' * 20)    

for n in n1:
    if n % 2 == 0:
        print(n, end=' ')
print(f' foram os numeros pares encontrados')