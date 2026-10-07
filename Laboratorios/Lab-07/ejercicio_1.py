# Sebastián Casillas Portillo
# A01572449
# Ejercicio 1: Nivel Básico

n = int(input("Número de renglones: "))
m = int(input("Número de columnas: "))

if n >= 2 and m >= 2:
    matriz = []
    numero = 1
    for i in range(n):
        renglon = []
        for j in range(m):
            renglon.append(numero)
            numero += 1
        matriz.append(renglon)
    print("[ " + ", ".join(str(r) for r in matriz) + " ]")
else:
    print("Error")