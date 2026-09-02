# Sebastián Casillas Portillo
# A01572449
# Reto integrador: mini calculadora científica para hipotenusa de un triángulo
# Prompt usado: necesito que me ayudes a hacer un prompt para una calculadora científica para sacar la hipotenusa de un triangulo. Necesito que se utilcen entradas, que en el proceso se usen funciones predefinidad como las de math, operaciones aritméticas y f(strings). Para que la salida me de como resultado la hipotenusa de un triángulo.

import math


print("Calculadora científica: hipotenusa de un triángulo")
cateto_a = float(input("Ingresa la medida del primer cateto: "))
cateto_b = float(input("Ingresa la medida del segundo cateto: "))

suma_cuadrados = cateto_a ** 2 + cateto_b ** 2
hipotenusa = math.sqrt(suma_cuadrados)

print(f"La hipotenusa del triángulo es: {hipotenusa:.2f}")
