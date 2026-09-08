# Sebastián Casillas Portillo
# A01572449
# Act 1: lógico

# Tipo de error: LÓGICO
# Cómo lo detecté: el programa se ejecuta sin ningún error, pero el resultado es incorrecto. Comparé la salida obtenida contra la esperada y está mal, aparte de que lo da como un comentario.

def calcular_promedio(lista):
    return sum(lista) / len(lista)

promedio = calcular_promedio([85, 92, 78, 90])
print(f"Promedio: {promedio:.1f}")