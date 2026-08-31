# Sebastián Casillas Portillo
# A01572449
# Refactor a funciones
# Arreglar esto

def registro():
    quiz_1 = float(input('¿Cuál es tu calificación del primer quiz?'))
    quiz_2 = float(input('¿Cuál es tu calificación del segundo quiz?'))
    quiz_3 = float(input('¿Cuál es tu calificación del tercer quiz?'))
    quiz_4 = float(input('¿Cuál es tu calificación del cuarto quiz?'))
    return [quiz_1, quiz_2, quiz_3, quiz_4]

def calcula_promedio(calificaciones):
    return 