# Sebastián Casillas Portillo
# A01572449
# Ejercicio 4: Nivel Intermedio

x1= int(input("Ingresa el primer número:"))
x2= int(input("Ingresa el segundo número:"))
x3= int(input("Ingresa el tercer número:"))

if x1 <= x2 and x1<= x3:
    menor = x1
    if x2 <= x3:
        medio = x2
        mayor = x3
    else:
        medio = x3
        mayor = x2
elif x1 >= x2 and x1 >= x3:
    mayor = x1
    if x2 <= x3:
        menor = x2
        medio = x3
    else:
        menor = x3
        medio = x2
else:
    medio = x1
    if x2 <= x3:
        menor = x2
        mayor = x3
    else:
        mayor = x2
        menor = x3


print(f"Los numeros ordenados de menor a mayor son {menor}, {medio}, {mayor}")
