# Sebastián Casillas Portillo
# A01572449
# Ejercicio 15: Nivel intermedio

numero = int(input('Escribe un número entero positivo con lo dígitos que queiras.'))

digitos = 0
while numero > 0:
    numero = numero // 10
    digitos += 1

print(f"El número introducido tiene {digitos} dígitos.")