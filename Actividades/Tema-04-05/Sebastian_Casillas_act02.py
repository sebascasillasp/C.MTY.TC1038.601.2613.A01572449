# Sebastián Casillas Portillo
# A01572449
# Debug python

# Solicitar datos de dos estudiantes
nombre1 = input("Ingrese el nombre del estudiante 1: ")
nombre2 = input("Ingrese el nombre del estudiante 2: ")

# Solicitar las 4 calificaciones de cada estudiante
def pedir_calificaciones(nombre):
    calificacion1 = float(input(f"Ingrese la calificación 1 de {nombre}: "))
    calificacion2 = float(input(f"Ingrese la calificación 2 de {nombre}: "))
    calificacion3 = float(input(f"Ingrese la calificación 3 de {nombre}: "))
    calificacion4 = float(input(f"Ingrese la calificación 4 de {nombre}: "))
    return [calificacion1, calificacion2, calificacion3, calificacion4]


cal1 = pedir_calificaciones(nombre1)
cal2 = pedir_calificaciones(nombre2)

# Calcular promedios
promedio1 = sum(cal1) / 4
promedio2 = sum(cal2) / 4

# Determinar cuál promedio es mayor y cuánto supera
estudiantes = [(promedio1, nombre1), (promedio2, nombre2)]
promedio_mayor, nombre_mayor = max(estudiantes, key=lambda x: x[0])
promedio_menor, nombre_menor = min(estudiantes, key=lambda x: x[0])
diferencia = promedio_mayor - promedio_menor

# Mostrar resultados
print(f"El promedio mayor es el de {nombre_mayor} con {promedio_mayor:.2f} puntos.")
print(f"El promedio de {nombre_menor} es menor por {diferencia:.2f} puntos.")
print(f"{nombre_mayor} supera a {nombre_menor} por {diferencia:.2f} puntos.")

# Casos de prueba de caja negra
#
# Caso 1: promedios diferentes
# Entrada: Ana, Luis, 8, 9, 10, 9, 7, 8, 7, 8
# Salida esperada: Ana obtiene 9.00; Luis obtiene 7.50; diferencia 1.50.
#
# Caso 2: promedios iguales
# Entrada: María, Pedro, 8, 8, 8, 8, 8, 8, 8, 8
# Salida esperada: ambos obtienen 8.00; diferencia 0.00.
#
# Caso 3: calificaciones decimales y segundo estudiante con mayor promedio
# Entrada: Sofía, Carlos, 6.5, 7.5, 8.0, 7.0, 9.0, 9.5, 8.5, 9.0
# Salida esperada: Carlos obtiene 9.00; Sofía obtiene 7.25; diferencia 1.75.


