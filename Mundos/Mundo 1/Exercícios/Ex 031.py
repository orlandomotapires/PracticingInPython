distancia = float(input('Insira a distancia da viagem em KM\n'))
if distancia <= 200:
    precopass = 0.50 * distancia
else:
    precopass = 0.45 * distancia

print('O preço da sua viagem ficou: {}'.format(precopass))  
      
