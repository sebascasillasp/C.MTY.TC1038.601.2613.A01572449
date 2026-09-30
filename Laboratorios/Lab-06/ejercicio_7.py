# Sebastián Casillas Portillo
# A01572449
# Ejercicio 7

def dibuja_linea (n):
    print('A' * n)

def main ():
    n= int(input('Número de líneas: '))
    for i in range (1, n+1):
        dibuja_linea (i)

main()
