velocarro = float(input('Insira a velocidade do carro em quilometros por hora!\n'))
if velocarro > 80:
    velocidadeex = velocarro - 80
    muta = velocidadeex * 7
    print('Você foi mutado em: {}'. format(muta))
else:
    print('Sua velocidade esta dentro do limite da rodovia')    