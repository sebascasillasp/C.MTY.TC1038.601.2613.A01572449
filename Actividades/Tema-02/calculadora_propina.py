# Sebastián Casillas Portillo
# A01572449
# Calculadora de propina (sin uso de ia)
input_montototal = float(input('Por favor, dígame el monto total de la cuenta: '))
input_propina = float(input('¿Cuánta propina desea dejar? (como porcentaje):'))
resultado_con_propina = input_montototal + (input_montototal * (input_propina)/100)
input_redondeado_con_propina = round(resultado_con_propina, 2)
print('El total de la cuenta con propina es: ' + str(input_redondeado_con_propina))