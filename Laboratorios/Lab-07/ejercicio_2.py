# Sebastián Casillas Portillo
# A01572449
# Ejercicio 2: Nivel Básico


def crea_matriz_numeros(n):
    matriz = []
    for i in range(n):
        renglon = []
        for j in range(n):
            renglon.append(i)
        matriz.append(renglon)
    return matriz

def muestra_matriz(matriz):
    for renglon in matriz:
        print("  ".join(str(x) for x in renglon))

n = int(input("Tamaño de la matriz cuadrada: "))

if n >= 2:
    matriz = crea_matriz_numeros(n)
    muestra_matriz(matriz)
else:
    print("Error")