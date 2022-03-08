numeros = ('zero','um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numesc = perg = 0
while True:
    numesc = int(input('Digite um numero entre 0 e 20: '))
    while (numesc < 0) | (numesc > 20):
        print('Insira um valor valido')
        numesc = int(input('Digite um numero entre 0 e 20: '))
    print(f'Voce digitou o número {numeros[numesc]}') 
    perg = str(input('Deseja continuar ? [N/S]\n')).upper().strip()[0]
    while perg not in 'NS':
        print('Insira uma resposta válida')
        perg = str(input('Deseja continuar ? [N/S]\n')).upper().strip()[0]

    if perg == 'N':
        break