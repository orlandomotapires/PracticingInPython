b = a = 0
def ate(a, b):
  print(f'Controle de terrenos')
  print('-='*30)
  a = float(input("Largura (Metros): "))
  b = float(input("Comprimento (Metros): "))
  area = a * b
  print(f'A area do terreno de largura {a} e comprimento {b} é {area}M^2')

ate(a, b)