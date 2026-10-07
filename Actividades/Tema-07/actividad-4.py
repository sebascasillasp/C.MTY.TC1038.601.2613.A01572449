# Sebastián Casillas Portillo
# A01572449
# Actividad 4: Busca, ordena y compara

movies= ['Coco','Dune','Up','Wall-E']
run_time= [105, 155, 96, 98]
def longest_movie(movies, run_time):
    if len(movies)==0 or len(run_time)==0:
        return None
    if len(movies)!=len(run_time):
        return None
    longest_index= 0
    for i in range(1, len(run_time)):
        if run_time[i]>run_time[longest_index]:
            longest_index= i
    return movies[longest_index]

movies= ['Coco','Dune','Up','Wall-E']
run_time= [105, 155, 96, 98]
print(movies, longest_movie(movies, run_time))
print(sorted(movies))