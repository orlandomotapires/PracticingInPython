import random 
tentativas = 0
lista = [0,1,2,3,4,5,6,7,8,9,10]
numc = random.choice(lista)
numu = 50
print('O computador escolheu: {}'. format(numc))
while numu != numc:
    numu = int(input('Escolha um numero entre {} a {}\n'.format(lista[0], lista[10])))
    if numu == numc:
        tentativas += 1
        print('Acertou jovem garfanhoto!')
    else:
        tentativas += 1
        print('Errrou!') 
print('Voce acertou na {} tentativa(s)!'.format(tentativas))        