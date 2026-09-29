# Sebastián Casillas Portillo
# A01572449
# Reto de formula real

pi= 3.1416

radio= float(input("¿Cual es el radio del círculo?"))
area= pi * radio ** 2
print (f"El área del circulo es {area}")

# Tal vez esta opción sea mejor porque usa una función y permite reutilizar
# la fórmula del círculo para calcular el área.
def calcular_area_circulo(radio):
	return pi * radio ** 2

print("Tal vez esta opción sea mejor para sacar el área:")
radio_mejorado = float(input("Ingresa nuevamente el radio del círculo: "))
area_mejorada = calcular_area_circulo(radio_mejorado)
print(f"El área del círculo usando la fórmula es {area_mejorada}")

# La formula usada viene de la fórmula del área del círculo que es pi por radio al cuadrado.

# Prompt usado: El código que está arriba sirve para sacar el área de un círculo, necesito que la mejores, no la borres y hagas una opción de print que diga que tal vez esta opción es mejor para sacar el área. Necesito que pidas el radio como entrada y que uses la fórmula del círculo.
