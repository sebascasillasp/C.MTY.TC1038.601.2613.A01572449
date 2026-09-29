# Sebastián Casillas Portillo
# A01572449
#Actividad 04: cosas que copilot ve y tu no
# Prompt para copilot: #  Sugiere 3 casos de prueba adicionales (de caja negra) para la siguiente función, que no estén ya cubiertos por estos casos: lista típica [85, 92, 78, 90], un solo valor [100], todos iguales [70, 70, 70, 70], y lista vacía []. Para cada caso nuevo dame: la entrada, la salida esperada, y por qué es un caso de prueba relevante (qué comportamiento distinto de la función pone a prueba).
# def calcular_estadisticas(lista):
#    promedio = sum(lista) / len(lista)
#    return promedio, max(lista), min(lista)

def calcular_estadisticas(lista):
    promedio = sum(lista) / len(lista)
    return promedio, max(lista), min(lista)

# Casos de prueba adicionales:
# 1. Entrada: [0, -5, 10]
#    Salida esperada: (1.6666666666666667, 10, -5)
#    Relevancia: prueba valores positivos, negativos y cero.
#
# 2. Entrada: [1.5, 2.5, 3.5]
#    Salida esperada: (2.5, 3.5, 1.5)
#    Relevancia: prueba el manejo de números decimales.
#
# 3. Entrada: [-100, -50, -75]
#    Salida esperada: (-75.0, -50, -100)
#    Relevancia: prueba el cálculo cuando todos los valores son negativos.




