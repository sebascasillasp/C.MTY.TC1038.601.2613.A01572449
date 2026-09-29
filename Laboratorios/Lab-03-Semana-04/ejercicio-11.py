# Sebastián Casillas Portillo
# A01572449
# Ejercicio 11

num1= int(input('Dime un número:'))
num2= int(input('Dime otro número:'))
num3= int(input('Dime otro número:'))

num_suma= num1 + num2

if (num3 != 0 and num_suma % num3 == 0):
    print(True)
    print(f'La suma de {num1} sumado a {num2} es múltiplo de {num3}')
else:
    print(False)
    print(f'La suma de {num1} sumado a {num2} no es múltiplo de {num3}')