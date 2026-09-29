# Sebastián Casillas Portillo
# A01572449
# Peso

peso_inicial = float(input("¿Cuál es tu peso?"))
peso_final = float(input("¿Cuánto quieres pesar?"))
meses = int(input("¿En cuánto quieres llegar a tu meta?"))

kilos_por_mes = (peso_inicial - peso_final) / meses

print("Tienes que bajar",kilos_por_mes, "por mes.")