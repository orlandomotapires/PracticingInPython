import random
import time
jogos = c = 0
sorteados = list()
listsort = list()
jogos = int(input('Quantos jogos seram gerados: '))
while c != jogos:
    for i in range(0,6):
        listsort.append(random.randint(0,60))
    c += 1 
    listsort.sort()
    if c == 1:
        print(f'Sorteando {jogos} jogos')   
    print(f'Jogo {c}: {listsort}')
    listsort.clear()
    time.sleep(1)   
    if c == jogos:
        print('Boa sorte')
    