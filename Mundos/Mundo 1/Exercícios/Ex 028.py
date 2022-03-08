import random 
lista = [0,1,2,3,4,5]
numc = random.choice(lista)
print(numc)
numu = int(input('Escolha um numero entre 0 a 5\n'))
if numu == numc:
    print('Acertou jovem garfanhoto!')
else:
    print('Errrou!')    