c = s = n1 = 0
while n1 != 999:
    n1 = int(input('Insira um valor para aderir a soma ou insira 999 para fechar o programa\n'))
      
    if n1 == 999:
        break
    
    s += n1
    c += 1
print(f'Foram digitados {c} números e a soma entre eles vale {s}')    