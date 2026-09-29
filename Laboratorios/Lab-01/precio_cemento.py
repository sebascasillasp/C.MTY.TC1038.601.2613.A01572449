# Sebastián Casillas Portillo
# A01572449
# Precio cemento

bultos = int(input("¿Cuántos bultos de cemento va a comprar? "))
precio_bulto = float(input("¿Cuál es el precio por bulto de cemento? "))

precio_antes_impuestos = bultos * precio_bulto
impuestos = precio_antes_impuestos * 0.16
total = precio_antes_impuestos + impuestos

print("Precio antes de impuestos:", precio_antes_impuestos)
print("Impuestos:", impuestos)
print("Total a pagar:", total)