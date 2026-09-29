# Sebastián Casillas Portillo
# A01572449
# Reflexiones tema 03

# ¿Qué criterio usaste para decidir dónde "cortar" tu programa en funciones? Si un compañero hubiera dividido el mismo programa, ¿crees que habría hecho exactamente los mismos cortes? ¿Por qué sí o no?
# Corté el programa según cada tarea con propósito claro (pedir datos, calcular, mostrar) un compañero podría dividirlo distinto porque no hay una única forma correcta de hacerlo.

# En la Actividad 2, una variable "dejó de existir" en cuanto la función terminó. ¿Qué tuviste que cambiar en tu forma de pensar el programa para entenderlo? ¿En qué otras situaciones —no de programación— algo solo tiene sentido dentro de un contexto limitado?
# Tuve que entender que las variables locales solo viven mientras la misma función, como unc histe local que solo hace sentido dentro de un grupo.

# Compara tu plan escrito en el paso 1 con lo que Copilot terminó proponiendo: ¿en qué se pareció? ¿en qué se diferenció? Si hubieran sido muy distintos, ¿con qué criterio decidirías cuál división usar?
# Se pareció en las funciones de calcular, comparar, mostrar y se diferenció en detalles de nombres o parámetros, usaría la división más clara y reutilizable.

# Reutilizaste calcular_estadisticas() de la Actividad 1 sin cambiarle una línea. ¿Qué tuvo que ser cierto sobre cómo la escribiste originalmente para que fuera reutilizable así, sin ajustes?
# Tuvo que recibir sus datos y regresar el resultado con return, sin depender de variables externas ni imprimir directamente.

# Instalaste y usaste una biblioteca escrita por alguien que no conoces, sin leer su código fuente. ¿Qué tuviste que confiar para hacerlo? ¿Se parece o se diferencia de confiar en una función que te sugiere Copilot?
# Sí, descargue pygame y la verdad está muy interesante. Confié en la comunidad que la usa.

# Compara el programa con el que empezaste hoy (todo en un bloque) contra el que tienes ahora (dividido en funciones, con una biblioteca externa, ejecutado desde terminal). ¿Qué se volvió más fácil? ¿Qué se volvió más complicado o tiene un costo nuevo?
# Se volvió más fácil de leer, probar y reutilizar, pero más complicado porque ahora hay que diseñar qué recibe y regresa cada función y confiar en herramientas externas.