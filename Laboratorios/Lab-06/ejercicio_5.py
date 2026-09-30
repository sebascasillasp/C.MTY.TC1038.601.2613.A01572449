# Sebastián Casillas Portillo
# A01572449
# Ejercicio 5:

def dibuja_linea (caracter, cantidad):
    linea= (caracter * cantidad)
    return linea

car = input('Caracter: ')
cant= int(input('Cantidad: '))
resultado = dibuja_linea(car, cant)
print(resultado)

