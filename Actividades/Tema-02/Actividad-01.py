# Sebastián Casillas Portillo
# A01572449
# Actividad en clase

# Constantes
COSTO_ENVIO= 10
# Entrada
costo_producto= float(input("Cuanto es el costo de tu producto?"))
cantidad_productos= int(input("Cuántos envíos vas a realizar?"))
# Proceso
costo_total= (costo_producto * cantidad_productos) + COSTO_ENVIO
# Salida
print("El costo total de tu producto es:", costo_total)