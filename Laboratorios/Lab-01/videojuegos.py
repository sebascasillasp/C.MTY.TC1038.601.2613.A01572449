# Sebastián Casillas Portillo
# A01572449
# Videojuegos

juegos_nuevos = int(input("¿Cuántos juegos nuevos va a comprar? "))
juegos_usados = int(input("¿Cuántos juegos usados va a comprar? "))

precio_nuevo = 1000
precio_usado = 350

total = (juegos_nuevos * precio_nuevo) + (juegos_usados * precio_usado)

print("El total de la compra es:", total)