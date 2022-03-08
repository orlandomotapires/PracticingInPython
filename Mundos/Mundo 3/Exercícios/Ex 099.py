numeros = list()
maximo = 0 
def maior():
  while True:
    numeros.clear()
    qnt = int(input('Quantos valores deseja informar: '))
    for c in range(0, qnt):
      numeros.append(int(input('Insira um valor: ')))
    
    for k in numeros:
      print(f'{k} ', end = '')
    print(f'Foram informados {qnt} valores.')
    print(f'O maior valor informado foi {max(numeros)}.')

    perg = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while perg not in 'NS':
      print('Resposta invalida! Tente novamente. ')
      perg = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    
    if perg == "N":
      break
    
maior()