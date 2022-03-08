import moeda107

p = float(input("Insira o preço R$: "))
print(f'A metade de R${moeda107.moeda(p)} é R${moeda107.moeda(moeda107.metade(p))}')
print(f'O dobro de R${moeda107.moeda(p)} é R${moeda107.moeda(moeda107.dobro(p))}')
print(f'O Aumento de R${moeda107.moeda(p)} é R${moeda107.moeda(moeda107.aumentar(p, 10))}')
print(f'A redução de R${moeda107.moeda(p)} é R${moeda107.moeda(moeda107.diminuir(p, 10))}')