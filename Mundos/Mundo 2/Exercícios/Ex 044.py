preconormal = float(input('Insira o preço comum do produto\n'))
forma = int(input('Qual forma de pagamento deseja? 1 para a vista no dinheiro ou cheque, 2 para a vista no cartao, 3 para ate 2x no cartao e 4 para 3x ou mais no cartao\n'))
f1 = preconormal * 0.9
f2 = preconormal * 0.95
f3 = preconormal 
f4 = preconormal * 1.2
if forma == 1:
    print('O seu produto que custava {}, agora vai custar {}'. format(preconormal, f1))
elif forma == 2:
    print('O seu produto que custava {}, agora vai custar {}'. format(preconormal, f2))    
elif forma == 3:
    print('O seu produto que custava {}, agora vai custar {}'. format(preconormal, f3))
elif forma == 4:
    print('O seu produto que custava {}, agora vai custar {}'. format(preconormal, f4))    