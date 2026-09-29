# Sebastián Casillas Portillo
# A01572449
# Formulario interactivo de registro

nombre= input("¿Cual es tu nombre?")
carrera= input("¿Carrera?")
promedio= float(input("¿Promedio?"))

bono_participacion= 0.5
promedio +=bono_participacion

print (f"{nombre} estudia la carrera de {carrera}")
print (f"El romedio final de {nombre} es {promedio}")