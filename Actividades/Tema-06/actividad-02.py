# Sebastián Casillas Portillo
# A01572449
# Ejemplos For

# Ejercicio 1:
for i in range (10):
    print(f'iteración {i}')

suma = 0

# Ejercicio 2:
filas = int(input('¿Cuantas filas quieres?'))
for i in range(1, filas + 1):
    print('hola'* i)

#Ejercicio 3:
filas = int(input('¿Cuántas filas quieres?'))
for i in range (filas + 1, 1, -1):
    print('$' * i)

# Ejercicio 3: 
for i in range (50, 0, -5):
    print(i)

# Ejercicio 4:
import random
clave = random.randint (1, 10)
for intento in range (1,4):
    numero = int(input('Adivina el número del 1 al 10: '))
    if numero == clave:
        print ('Adivinaste :)')
    elif numero < clave:
        print ('Intenta con un número más grande.')
    else:
        print('Intenta con un número más pequeño.')
    