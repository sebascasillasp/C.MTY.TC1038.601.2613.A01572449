# Sebastián Casillas Portillo
# A01572449
# Actividad 8: Versión final
# Prompt para Copilot: tengo estas piezas de un reporte de calificaciones y quiero que propongas como estructurarlo todo junto en un solo programa limpio: una funcion que calcule promedio, nota_max y nota_min de una lista, que clasifique el promedio en letra (A, B, C, Reprobado), y que si es Aprobado (70+) tambien revise si merece Mencion honorifica (promedio >= 95 y nota_min >= 90). Dame la estructura completa, yo despues decido que ajustar. Ajusté los nombres de variables para que coincidieran con mi función ya corregida (Actividad 1), y mantuve la decisión anidada de la Actividad 7 en vez de usar if/elif/else planos, porque necesitaba dos niveles de condición.

def calcular_estadisticas(lista):
    promedio = sum(lista) / len(lista)
    return promedio, max(lista), min(lista)

calificaciones = [85, 92, 78, 90]
promedio, nota_max, nota_min = calcular_estadisticas(calificaciones)

print(f"Promedio: {promedio:.1f}")
print(f"Nota máxima: {nota_max}")
print(f"Nota mínima: {nota_min}")

if promedio >= 70:
    if promedio >= 95 and nota_min >= 90:
        print("Aprobado — Mención honorífica")
    else:
        print("Aprobado")
else:
    print("Reprobado")