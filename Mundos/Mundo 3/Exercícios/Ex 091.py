from random import randint
from time import sleep
from operator import itemgetter
resultados = {}
resultados['jogador 1'] = randint(1,6)
resultados['jogador 2'] = randint(1,6)
resultados['jogador 3'] = randint(1,6)
resultados['jogador 4'] = randint(1,6)
ranking = list()
for k, v in resultados.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)  
ranking = sorted(resultados.items(), key = itemgetter(1), reverse = True)
print('-='*30)
print('==RANKING DO JOGADORES==')
for i, v in enumerate(ranking):
    print(f' {i+1} lugar: {v[0]} com {v[1]}.')
    







