resto = valortotal = perg = c50 = c20 = c10= c1 = soma = 0
while perg != 'N':
    
    valortotal = int(input('Insira o valor a ser sacado '))
    while valortotal < 0:
        print('Insira um valor valido')
        valortotal = int(input('Insira o valor a ser sacado '))
    
    perg = str(input('Deseja sacar mais dinheiro ? [S/N]')).upper().strip()[0]
    while (perg != 'N') and (perg != 'S'):
        print('Insira um valor valido')
        perg = str(input('Deseja sacar mais dinheiro ? [S/N]')).upper().strip()[0]
   
    soma += valortotal
    
    if soma >= 50:
        c50 = soma // 50
        resto = soma - c50*50

    if resto >=20:
        c20 = resto //20
        resto = resto - c20*20
    
    if resto >= 10:
        c10 = resto //10
        resto = resto - c10*10

    if resto < 10:
        c1 = resto

    if perg == 'N':
        break

print(f"""
O TOTAL VALOR SACADO FOI {soma}
[{c50}] NOTAS DE R$50.00
[{c20}] NOTAS DE R$20.00
[{c10}] NOTAS DE R$10.00
[{c1}] NOTAS DE R$ 1.00""")
