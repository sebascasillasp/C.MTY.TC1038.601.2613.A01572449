# Sebastián Casillas Portillo
# A01572449
# Ejercicio 10: Avanzado

dia1 = int(input("Ingresa el día de la primera fecha: "))
mes1 = int(input("Ingresa el número de mes de la primera fecha: "))
dia2 = int(input("Ingresa el día de la segunda fecha: "))
mes2 = int(input("Ingresa el número de mes de la segunda fecha: "))

if mes1 < mes2:
    print('La fecha 1 ocurre primero')
elif mes1> mes2:
    print('La fecha 2 ocurre primero')
else:
    if dia1 < dia2:
        print('La fecha 1 ocurre primero')
    elif dia1 > dia2:
        print('La fecha 2 ocurre primero')
    else:
        print('Las fechas son iguales')