# Sebastián Casillas Portillo
# A01572449
# Mi control de gastos

def pedir_entero_positivo(mensaje):

    entrada = ''
    while not entrada.isdigit():
        entrada = input(mensaje)
        if not entrada.isdigit():
            print(f"Error: '{entrada}' no es un número entero positivo. Intenta de nuevo.")
    return int(entrada)


num_categorias = 0
while num_categorias < 1:
    num_categorias = pedir_entero_positivo('¿Cuántas categorías vas a usar? ')
    if num_categorias < 1:
        print("Debe haber al menos 1 categoría.")


list_categorias = []
total_gasto = []


for i in range(num_categorias):
    categoria = input(f'\nEscribe el nombre de la categoría {i+1}: ')
    list_categorias.append(categoria)
    
    gastos_categoria = []
    gasto = -1

    while gasto != 0:
        gasto = pedir_entero_positivo('Gasto (escribe 0 para terminar): ')
        if gasto != 0:
            gastos_categoria.append(gasto)

    total_gasto.append(gastos_categoria)

def calcular_estadisticas(gastos):
    total = sum(gastos)
    if len(gastos) == 0:
        promedio = None
    else:
        promedio = total // len(gastos)
    return len(gastos), total, promedio

def clasificacion(total):
    if total < 3000:
        return "Bajo"
    elif total <= 7000:
        return "Medio"
    else:
        return "Alto"


for i in range(num_categorias):
    cantidad, total, media = calcular_estadisticas(total_gasto[i])
    print(f"{list_categorias[i]} - Gastos: {cantidad} - Total: {total} - Promedio: {media}")

#total_general = sum(sum(gastos) for gastos in total_gasto)

totales = list(map(sum, total_gasto))
total_general = sum(totales)      
categoria_mayor = list_categorias[totales.index(max(totales))]

print(f"El total de las {len(list_categorias)} categorias es de {total_general}")

print(f"Donde más gastaste fue en la categoria {categoria_mayor}")

print(f"Nivel de gasto al mes: {clasificacion(total_general)}")