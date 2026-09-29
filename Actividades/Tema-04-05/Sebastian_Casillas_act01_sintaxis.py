# Sebastián Casillas Portillo
# A01572449
# Act 1: sintaxis

# Cómo lo detecté: al ejecutar el archivo, Python arrojó un SyntaxError ("expected ':'"), ya que a la definición de la función le faltaba el símbolo ':' al final de la línea.

def calcular_promedio(lista):
    return sum(lista) / len(lista)

calcular_promedio([85, 92, 78])