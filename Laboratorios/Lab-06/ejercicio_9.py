# Sebastián Casillas Portillo
# A01572449
# Ejercicio 9:

n = int(input('Numero: '))

if abs(n) >= 1000000:
    print("numero demasiado largo")
else:
    signo = -1 if n < 0 else 1
    n = abs(n)
    inverso = 0
    while n > 0:
        digito = n % 10
        inverso = inverso * 10 + digito
        n = n // 10
    print(signo * inverso)
    