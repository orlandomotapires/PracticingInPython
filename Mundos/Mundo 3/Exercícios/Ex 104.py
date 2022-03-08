def leiaint(a):
  b = str(input(f'{a}'))
  while True:
    if b.isdigit():
      return b 
      break 
    else:
      print('Erro digite um numero inteiro valido')
      b = input('Digite um numero ')  

while True:
  n = leiaint(('Digite um numero: '))
  print(f'Voce acabou de digitar o numero {n}')

  perg  = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
  while perg not in 'SN':
    print('Erro digite um numero inteiro valido')
    perg  = str(input('Deseja continuar? [S/N]')).upper().strip()[0]

  if perg in 'N':
    break

 