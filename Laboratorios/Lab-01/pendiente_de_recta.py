# Sebastián Casillas Portillo
# A01572449
# Pendiente de una recta

x1 = float(input("Escribe x1: "))
y1 = float(input("Escribe y1: "))
x2 = float(input("Escribe x2: "))
y2 = float(input("Escribe y2: "))

if x2 == x1:
	print("La pendiente no está definida.")
else:
	pendiente = (y2 - y1) / (x2 - x1)
	print("La pendiente es:", pendiente)

