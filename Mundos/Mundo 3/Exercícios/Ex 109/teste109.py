import moeda109

p = float(input("Insira o preço R$: "))
print(f'A metade de {moeda109.moeda(p)} é {moeda109.metade(p, True)}')
print(f'O dobro de {moeda109.moeda(p)} é {moeda109.dobro(p, True)}')
print(f'O Aumento de {moeda109.moeda(p)} é {moeda109.aumentar(p, 10, True)}')
print(f'A redução de {moeda109.moeda(p)} é {moeda109.diminuir(p, 10, True)}')
