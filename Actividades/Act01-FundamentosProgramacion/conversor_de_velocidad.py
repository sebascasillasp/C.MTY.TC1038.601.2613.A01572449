# Se necesita saber la velocidad promedio de un ciclista, con un input que será solo los km y el tiempo en horas. Con esto sacaré la velocidad en km/h y posteriormente lo cambiaré a m/s.

# Para hacer esto simplemente se ocupan los km recorridos y las horas.

# Primero dividiré los km entre las horas que nos digan, para sacar los km/h y para cambiarlo a m/s lo multiplicaré por 1000 y dividiré entre 3600.

km_recorridos = float(input("Ingresa los km recorridos: "))
tiempo_horas = float(input("Ingresa el tiempo en horas: "))
velocidad_kmporh = km_recorridos / tiempo_horas
print('Tu velocidad es: ' + str(velocidad_kmporh))
velocidad_ms = (velocidad_kmporh * 1000) / 3600
print ('Tu velocidad es: ' + str(velocidad_ms))