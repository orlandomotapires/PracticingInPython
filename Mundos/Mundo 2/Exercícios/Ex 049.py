import time
num = float(input('Digite o numero que deseja saber a tabuada!!\n'))
ate = int(input('Ate qual numero voce deseja saber a tabuada do numero escolhido ?\n'))

for c in range(0, ate+1):   
    print(num*c)