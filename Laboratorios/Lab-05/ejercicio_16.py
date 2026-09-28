# Sebastián Casillas Portillo
# A01572449
# Ejercicio 16: Nivel intermedio 

numero = int(input("Introduce un número entero con la cantidad de digitos que quieras:"))


if numero < 0:
    numero = -numero

suma = 0
while numero > 0:
    ultimo = numero % 10
    suma += ultimo
    numero = numero // 10

print("La suma de los dígitos del número es:", suma)