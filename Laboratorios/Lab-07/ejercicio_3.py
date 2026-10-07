# Sebastián Casillas Portillo
# A01572449
# Ejercicio 3: Nivel Básico

def determinante(matriz):
    a = matriz[0][0]
    b = matriz[0][1]
    c = matriz[1][0]
    d = matriz[1][1]
    return a * d - c * b

def crea_matriz():
    matriz = []
    for i in range(2):
        renglon = input(f"Valores del renglón {i + 1} (separados por espacios): ").split()
        matriz.append([int(x) for x in renglon])
    return matriz

def main():
    matriz = crea_matriz()
    if len(matriz[0]) != 2 or len(matriz[1]) != 2:
        print("Error: La matriz no es una matriz de 2x2")
    else:
        print("El determinante de la matriz ingresada es:", determinante(matriz))

main()