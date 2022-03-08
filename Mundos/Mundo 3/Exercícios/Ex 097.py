def escreva():
  while True:  
    msg = str(input("Digite a mensagem: "))
    tam = len(msg)
    print("-" * (tam + 2 )) 
    print(f' {msg}')
    print("-" * (tam + 2))
    
    perg = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    while perg not in "NS":
      print('Resposta invalida! Tente novamente', end = '')
      perg = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if perg == 'N':
      break  