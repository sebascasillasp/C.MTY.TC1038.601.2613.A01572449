# Sebastián Casillas Portillo
# A01572449
# Divide y vencerás

# Prompt para Copilot:
#Necesito hacer un programa en el cual haya dos estudiantes, usando un print input, pide la calificacion de 4 calificaciones (cada uno). Calcula el promedio separandolo por estudiante con multiplicaciones y dividiendo entre 4. Y muestra el promedio mayor sin usar if.

# Estudiante 1
nombre1 = input("Ingresa el nombre del estudiante 1: ")
calificacion1 = float(input(f"Ingresa la calificación 1 de {nombre1}: "))
calificacion2 = float(input(f"Ingresa la calificación 2 de {nombre1}: "))
calificacion3 = float(input(f"Ingresa la calificación 3 de {nombre1}: "))
calificacion4 = float(input(f"Ingresa la calificación 4 de {nombre1}: "))

promedio1 = (calificacion1 + calificacion2 + calificacion3 + calificacion4) / 4

# Estudiante 2
nombre2 = input("Ingresa el nombre del estudiante 2: ")
calificacion5 = float(input(f"Ingresa la calificación 1 de {nombre2}: "))
calificacion6 = float(input(f"Ingresa la calificación 2 de {nombre2}: "))
calificacion7 = float(input(f"Ingresa la calificación 3 de {nombre2}: "))
calificacion8 = float(input(f"Ingresa la calificación 4 de {nombre2}: "))

promedio2 = (calificacion5 + calificacion6 + calificacion7 + calificacion8) / 4

promedio_mayor = max(promedio1, promedio2)
estudiante_mayor = (nombre1, nombre2)[(promedio1 < promedio_mayor) * 1]

print(f"Promedio de {nombre1}:", promedio1)
print(f"Promedio de {nombre2}:", promedio2)
print(f"El estudiante con el promedio más alto es: {estudiante_mayor}")
print(f"Promedio mayor: {promedio_mayor}")

