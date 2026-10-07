# Sebastián Casillas Portillo
# A01572449
# Ejercicio 9: Nivel Avanzado

def centro_matriz():
    n = int(input("Número de renglones: "))
    m = int(input("Número de columnas: "))

    matriz = []
    for i in range(n):
        renglon = []
        for j in range(m):
            renglon.append(int(input(f"Dato del renglón {i + 1}, columna {j + 1}: ")))
        matriz.append(renglon)

    centro = []
    for i in range(1, n - 1):
        renglon = []
        for j in range(1, m - 1):
            renglon.append(matriz[i][j])
        centro.append(renglon)
    return centro

centro = centro_matriz()

if len(centro) == 0:
    print("La submatriz correspondiente al centro de la matriz ingresada es: [ ]")
else:
    print("La submatriz correspondiente al centro de la matriz ingresada es: [ " + ", ".join(str(r) for r in centro) + " ]")