# Sebastián Casillas Portillo
# A01572449
# Act 2: semántico

# Cómo lo detecté: al ejecutar el archivo, Python arrojó un TypeError porque se le pasó un string ("85,92,78") a la función en lugar de una lista de números, y sum() no puede sumar los caracteres de un string así.

def calcular_promedio(lista):
    return sum(lista) / len(lista)

calcular_promedio([85, 92, 78])