n1 = int(input('Insira um numero: '))
c = 0 
ant = 0   
sucant = 1
while c != n1:
    c += 1   
    suc = sucant + ant      
    print(suc)
    ant = sucant
    sucant = suc
    
    

