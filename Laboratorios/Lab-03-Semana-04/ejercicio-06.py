# Sebastián Casillas Portillo
# A01572449
# Ejercicio 6

persona1= int(input("Dime la edad de Pedro:"))
persona2= int(input("Dime la edad de Jorge:"))
persona3= int(input("Dime la edad de José:"))

if (persona1 < persona2 and persona1 < persona3):
    print(True)
    print('La primera persona (Pedro) es la más joven.')
else:
    print(False)
    print('La primera persona (Pedro) no es la más joven.')