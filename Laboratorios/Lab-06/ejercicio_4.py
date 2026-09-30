# Sebastián Casillas Portillo
# A01572449
# Ejercicio 4:
money= int(input('¿Cuánto dinero vas a meter en la cuenta de inversión?'))
rate= int(input('Rendimiento anual: '))

if money < 0 or rate < 0:
    print('Error en los datos')

m_rate = rate / 12 /100

for i in range (12):
    money += money * m_rate

print(f'Al final del año tendras: {money}')