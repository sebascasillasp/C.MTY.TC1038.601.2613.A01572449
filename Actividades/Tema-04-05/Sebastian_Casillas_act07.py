# Sebastián Casillas Portillo
# A01572449
# Actividad 7: Anida una decisión

def calcular_estadisticas(lista):
    promedio = sum(lista) / len(lista)
    return promedio, max(lista), min(lista)

calificaciones = [85, 92, 78, 90]
promedio, nota_max, nota_min = calcular_estadisticas(calificaciones)

print(f"Promedio: {promedio:.1f}")
print(f"Nota máxima: {nota_max}")
print(f"Nota mínima: {nota_min}")

# Decisión anidada: solo si aprueba se evalúa la mención honorífica, así cada mensaje se imprime una sola vez.
if promedio >= 70:
    if promedio >= 95 and nota_min >= 90:
        print("Aprobado — Mención honorífica")
    else:
        print("Aprobado")
else:
    print("Reprobado")