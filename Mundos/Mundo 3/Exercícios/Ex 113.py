def leiaint(msg):
  while True:
    try: 
      a = int(input(msg))
    except(ValueError, TypeError):  
      print("\033[031mO numero digitado tem que ser obrigatoriamente um inteiro!\033[m") 
      continue
    except (KeyboardInterrupt):
      print('\033[031mEntrada de dados interrompida pelo usuário[m')
      return 0
    else:
      return a     

def leiafloat(msg):
  while True:
    try: 
      a = float(input(msg))
    except(ValueError, TypeError):  
      print("\033[031mO numero digitado tem que ser obrigatoriamente um float!\033[m") 
      continue
    except (KeyboardInterrupt):
      print('\033[031mEntrada de dados interrompida pelo usuário[m')
      return 0
    else:
      return a 

a = leiaint('Digite um valor inteiro: ')
b = leiafloat('Digite um valor float: ')
print(f"Valor de a: {a}; Valor de b: {b}")