from random import randint
from time import sleep

def sorteio():
  print(f'Sorteando os 5 valores: ', end = '')
  for c in range(0,5):
    numeros.append(randint(0, 10))
    print(f'{numeros[c]} ', end = '', flush = True)
    sleep(0.5)   
  print('')   

def somapar():
  soma = 0
  for k in numeros:
    if k % 2 == 0:
      soma += k
  print(f'O resultado da soma é: {soma}')

numeros = list()
sorteio()
somapar()