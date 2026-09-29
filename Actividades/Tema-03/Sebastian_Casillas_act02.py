# Sebastián Casillas Portillo
# A01572449
# Detective de alcance

def calcular_bono(sueldo):
    bono = sueldo * 0.10
    return bono

sueldo = 200000
bono = calcular_bono(sueldo)
print(f'El sueldo de ${sueldo:.2f} mas el bono es de ${sueldo + bono:.2f}')
