import moeda108

p = float(input("Insira o preço R$: "))
print(f'A metade de R${moeda108.moeda(p)} é R${moeda108.moeda(moeda108.metade(p))}')
print(f'O dobro de R${moeda108.moeda(p)} é R${moeda108.moeda(moeda108.dobro(p))}')
print(f'O Aumento de R${moeda108.moeda(p)} é R${moeda108.moeda(moeda108.aumentar(p, 10))}')
print(f'A redução de R${moeda108.moeda(p)} é R${moeda108.moeda(moeda108.diminuir(p, 10))}')