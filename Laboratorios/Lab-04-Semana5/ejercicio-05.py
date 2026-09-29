# Sebastián Casillas Portillo
# A01572449
# Ejercicio 5: Intermedio

peso= float(input("¿Cuál es tu peso en kg?"))
altura= float(input("¿Cuál es tu altura en metros?"))

indice = peso / altura**2

if indice < 20:
    clasificacion = 'PESO BAJO'
elif 20 <= indice < 25:
    clasificacion = 'PESO NORMAL'
elif 25 <= indice < 30:
    clasificacion = 'SOBREPESO'
elif 30 <= indice < 40:
    clasificacion = 'OBESIDAD'
else:
    clasificacion = 'OBESIDAD MÓRBIDA'

print(f'El índice de masa corporal es de {indice} por lo que el usuario tiene clasificación de {clasificacion}')

