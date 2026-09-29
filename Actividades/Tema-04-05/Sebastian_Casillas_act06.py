# Sebastián Casillas Portillo
# A01572449
# Actividad 6:
#Prompt para copilot: tengo un promedio y quiero clasificarlo en letra: A si es 90 o mas, B si es 80 a 89, C si es 70 a 79, y Reprobado si es menos de 70. hazme dos versiones: una usando if/elif/else otra usando match/case reutiliza la variable promedio que ya tengo, no me pidas que la vuelva a escribir

def calcular_estadisticas(lista):
    promedio = sum(lista) / len(lista)
    return promedio, max(lista), min(lista)

calificaciones = [85, 92, 78, 90]
promedio, nota_max, nota_min = calcular_estadisticas(calificaciones)

print(f"Promedio: {promedio:.1f}")
print(f"Nota máxima: {nota_max}")
print(f"Nota mínima: {nota_min}")

# Versión usando if/elif/else
if promedio >= 90:
    clasificacion_if = "A"
elif promedio >= 80:
    clasificacion_if = "B"
elif promedio >= 70:
    clasificacion_if = "C"
else:
    clasificacion_if = "Reprobado"

print(f"Clasificación (if/elif/else): {clasificacion_if}")

# Versión usando match/case
match promedio:
    case promedio if promedio >= 90:
        clasificacion_match = "A"
    case promedio if promedio >= 80:
        clasificacion_match = "B"
    case promedio if promedio >= 70:
        clasificacion_match = "C"
    case _:
        clasificacion_match = "Reprobado"

print(f"Clasificación (match/case): {clasificacion_match}")
