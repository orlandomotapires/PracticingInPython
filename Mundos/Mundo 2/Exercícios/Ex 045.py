import random
eu = int(input('Escolha um elemento entre 1 para pedra, 2 para papel e 3 para tesoura!\n'))
pc = random.randrange(1,3)
print(pc)


if (pc == 1) & (eu == 1):
    pc = 'Pedra'
    print('EMPATE, os dois jogadores escolheram {}'. format(pc))
elif (pc == 1) & (eu == 2):
    pc = 'Pedra'
    eu = 'Papel'
    print('VOCE VENCEU, o computador escolheu {} e voce escolheu {}'. format(pc, eu))    
elif (pc == 1) & (eu == 3):
    pc = 'Pedra'
    eu = 'Tesoura'
    print('O computador venceu :( , o computador escolheu {} e voce escolheu {}'. format(pc, eu))



elif (pc == 2) & (eu == 1):
    pc = 'Papel'
    eu = 'Pedra'
    print('O computador venceu :( , o computador escolheu {} e voce escolheu {}'. format(pc, eu))   
elif (pc == 2) & (eu == 2):
    pc = 'Papel'
    eu = 'Papel'
    print('EMPATE, os dois jogadores escolheram {}'. format(pc))      
elif (pc == 2) & (eu == 3):
    pc = 'Papel'
    eu = 'Tesoura'
    print('VOCE VENCEU, o computador escolheu {} e voce escolheu {}'. format(pc, eu)) 

elif (pc == 3) & (eu == 1):
    pc = 'Tesoura'
    eu = 'Pedra'
    print('VOCE VENCEU, o computador escolheu {} e voce escolheu {}'. format(pc, eu))     
elif (pc == 3) & (eu == 2):
    pc = 'Tesoura'
    eu = 'Papel'
    print('O computador venceu :( , o computador escolheu {} e voce escolheu {}'. format(pc, eu))      
elif (pc == 3) & (eu == 3):
    pc = 'Tesoura'
    eu = 'Tesoura'
    print('EMPATE, os dois jogadores escolheram {}'. format(pc))           