from time import sleep
def contador():
  print('-='* 30)
  print('Primeira Contagem')
  for c in range(0, 11, 1):
    print(f'{c} ', end = '', flush = True)
    sleep(0.5)

  print('')
  print('++'* 30)
  print('Segunda Contagem')
  for b in range (10, -2, -2):
    print(f'{b} ', end = '', flush = True)
    sleep(0.5)
    

  print('')
  print('//'* 30)
  print('Terceira Contagem')
  inicial = int(input('Qual o primeiro numero da contagem: '))
  final = int(input('Qual o último numero da contagem: '))
  ordemt = int(input('Insira como você deseja que a contagem seja feita: '))
  
  if ordemt == 0:
    ordem = -1
    ordemt = 1
  
  elif inicial > final and ordemt > 0:
    ordem = ordemt * -1
   
  elif ordemt < 0:
    ordem = ordemt 
    ordemt *= -1
  

  for k in range(inicial, final + ordem, ordem):
    if k == inicial:
      print(f'Contagem de {inicial} até {final} de {ordemt} em {ordemt}')
    print(f'{k} ', end = '', flush = True) 
      
contador()
print('Fim!')  