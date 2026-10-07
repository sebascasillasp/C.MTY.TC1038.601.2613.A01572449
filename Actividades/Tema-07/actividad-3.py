# Sebastián Casillas Portillo
# A01572449
# Actividad 3: La cartelera es una lista

cartelera = []
pelicula= ""

while pelicula.upper() != 'Fin':
    pelicula = input ('Dame el nombre de una película (Escribe Fin para terminar).').title()
    if pelicula in cartelera:
            print(f'La película {pelicula} ya existe en la lista')
    else:
          cartelera.append(pelicula)

for index, cartelera in enumerate (cartelera, 1):
      print(f'{index}-{pelicula}')
        
        