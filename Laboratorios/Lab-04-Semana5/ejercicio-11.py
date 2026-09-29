# Sebastián Casillas Portillo
# A01572449
# Ejercicio 11: Avanzado

angulo= int(input('Escribe un número entre 0 y 360:'))

if angulo == 90 or angulo == 180 or angulo == 270 or angulo == 360 or angulo == 0:
    print('El ángulo se encuentra en un eje')
elif 0< angulo < 90:
    print('El ángulo se encuentra en el cuadrante 1')
elif 90 < angulo < 180:
    print('El ángulo se encuentra en el cuadrante 2')
elif 180 < angulo < 270:
    print('El ángulo se encuentra en el cuadrante 3')
elif 270 < angulo < 360:
    print ('El ángulo se encuentra en el cuadrante 4')
else:
    print('El ángulo excede los cuadrantes')