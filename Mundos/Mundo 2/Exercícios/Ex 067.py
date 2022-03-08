n1 = val = res = c = 0
while n1 >= 0:
    n1 = int(input('Escolha um numero entre 1 a 10 para saber a tabuada: '))
    while c != 11:              
        if n1 < 0:
            break  

        res = n1 * val
        
        print(f'{n1} X {val} = {res}')    
        
        val += 1
        c += 1
   
    c = val = 0
    