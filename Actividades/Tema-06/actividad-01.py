# Sebastián Casillas Portillo
# A01572449
# Actividad 1: Contador del uno al 10

def validate_grade(grade_str):
    if grade_str != '-1':
        while not grade_str.isdigit():
            print(f'esto {grade_str} no es entero positivo')
            grade_str = input('Dame la calificación: ')
    return int(grade_str)

def validate_credits(credit_str):
    while credit_str not in valid_credits:
        print(f'los creditos validos son {valid_credits}')
        credit_str = input('Dame los créditos de la clase: ')
    return int(credit_str)



valid_credits = ['1','2','3','6','12']
grades = []
credits = []
courses = []
grade_str = input('Dame la calificación: ')
grade = validate_grade(grade_str)
if grade != -1:
    credit_str = input('Dame los créditos de la clase: ')
    credit = validate_credits(credit_str)
    course = input('Dame el nombre de la clase: ')

# voy a pedir la calificación hasta que tecleen -1
while grade != -1:
    credits.append(credit)
    grades.append(grade)
    courses.append(course)
    grade_str = int(input('Dame la calificación: '))
    grade = validate_grade(grade_str)
    if grade != -1:
        credit_str = int(input('Dame los créditos de la clase: '))
        credit = validate_credits(credit_str)
        course = input('Dame el nombre de la clase: ')

# valida que tenga calificaciones
if len(grades) > 0:
    # imprimir los valores
    index = 0
    sum_grades = 0
    while index < len(grades):
        print(f'{courses[index]} - {credits[index]} - {grades[index]}')
        sum_grades += grades[index] * credits[index]
        index += 1

    print(f'El promedio ponderado es: {sum_grades / sum(credits)}')