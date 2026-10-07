# Sebastián Casillas Portillo
# A01572449
# Ejercicio 5: Nivel Intermedio
n = int(input("Número de renglones: "))
m = int(input("Número de columnas: "))

if n >= 1 and m >= 1:
    matriz = []
    for i in range(n):
        renglon = []
        for j in range(m):
            renglon.append(int(input(f"Dato del renglón {i + 1}, columna {j + 1}: ")))
        matriz.append(renglon)

    sumas = []
    for j in range(m):
        suma = 0
        for i in range(n):
            suma += matriz[i][j]
        sumas.append(suma)

    print("La suma de los valores por columna corresponde a: [" + " ".join(str(s) for s in sumas) + "]")
else:
    print("Error")