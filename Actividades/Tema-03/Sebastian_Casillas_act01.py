# Sebastián Casillas Portillo
# A01572449
# Refactor a funciones

def registro():
    cal1 = float(input("Calificación 1: "))
    cal2 = float(input("Calificación 2: "))
    cal3 = float(input("Calificación 3: "))
    cal4 = float(input("Calificación 4: "))
    return [cal1, cal2, cal3, cal4]

def calcula_promedio(calificanes):
    return sum(calificaciones) / len(calificaciones)

def print(calificaiones):
    promedio = calcula_promedio(calificaciones)
    nota_max = max(calificaciones)
    nota_min = min(calificaciones)
    rango = nota_max - nota_min
    print("=" * 30)
    print(f"Reporte de {nombre}")
    print(f"Promedio: {promedio:.1f}")
    print(f"Máxima: {nota_max}  Mínima: {nota_min}")
    print(f"Rango: {rango:.1f}")

nombre = input("Nombre del estudiante: ")
calificaciones = registro()
print(calificaciones)