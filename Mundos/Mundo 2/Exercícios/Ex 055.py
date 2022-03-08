maiorpeso = 0
menorpeso = 0
menorpesoatual = 0
for c in range(0,5):
    peso = float(input('Digite o seu peso!\n'))
    
    if c == 0:
        maiorpeso = peso
        menorpeso = peso

    if peso < maiorpeso:
        menorpeso = peso 
    
    elif peso > maiorpeso:
        maiorpeso = peso  
     

print('O menor peso foi {}'. format(menorpeso))
print('O maior peso foi {}'. format(maiorpeso))   
