from time import sleep
def fatorial(a,show):
  """
  --> Calcula o fatorial de um número.
  a eh o numero cujo sera calculado o fatorial
  c eh a condicao de mostrar ou nao as contas
  retorna o valor do fatorial de um numero a
  
  """

  print(f'O fatorial de {b}: ', end = '')
  f = 1
  for d in range(a, 0 , -1):
    f*= d
    if c == 'T':     
      print(f'{f} ', end ='', flush = True)
      sleep(0.3)
  return f  
  
b =  int(input('Insira um valor para calculo de seu fatorial: '))
c = str(input('Deseja que a operacao seja mostrada ? [T/F] ')).upper().strip()[0]
fat =  fatorial(b, c)
if c == 'F':
  print(fat)  
help(fatorial)  