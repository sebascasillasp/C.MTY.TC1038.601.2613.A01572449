# Sebastián Casillas Portillo
# A01572449
# Ejercicio 13: Nivel anvanzado

# Para sumar un minuto teclea "s" y para terminar el programa teclea "t".
hora= int(input("¿Que hora es (sin minutos)?"))
minutos= int(input("¿Cuántos minutos van de esa hora?"))

letra = input("¿Qué letra escoges?")


while letra != "t":
    if letra == "s":
        minutos += 1
        if minutos == 60:
            minutos = 0
            hora += 1
            if hora == 24:
                hora = 0
        print (f"{hora}:{minutos}")
    else:
        print ("Esa no es una letra válida.")
    letra = input ("Escoge la letra 's' o 't'.")

