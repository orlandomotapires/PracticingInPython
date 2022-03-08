from datetime import date
def voto(nasc):
  
  if 16 <= 2021 - nasc < 18 or 2021 - nasc >= 65 :
    return 'OPCIONAL'
  elif 2021 - nasc < 16:   
    return 'NEGADO'
  elif 2021 - nasc >= 18:
    return 'OBRIGATORIO'  

nasc = int(input('Em que ano voce nasceu ? '))
idade = date.today().year - nasc 
condição = voto(nasc)
print(f'O cidadao tem {idade} anos e o voto é: {condição}') 