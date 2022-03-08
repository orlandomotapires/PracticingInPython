peso = float(input('Digite o seu peso!\n'))
altura = float(input('Digite sua altura em metros!\n'))
imc = peso / (altura * altura)
print(imc)
if imc < 18.5:
    print('ABAIXO DO PESO')
elif (imc >= 18.5) & (imc < 25):  
    print('Peso ideal')
elif (imc >= 25) & (imc < 30):  
    print('Sobre peso')
elif (imc >= 30) & (imc < 40):  
    print('OBESIDADE')      
elif imc > 40:
    print('Obesidade morbida!')  
