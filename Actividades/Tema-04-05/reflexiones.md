# Sebastián Casillas Portillo
# A10572449
# Reflexiones temas 4 y 5}

# ¿En qué momento identificaste el tipo de error antes de leer el mensaje completo? ¿Qué pista te lo dijo?
# Con el de sintaxis fue rápido, en cuanto vi que faltaba el ":" ya sabía que iba a tronar antes de correrlo. El semántico igual lo vi venir porque le estaban pasando un texto como si fuera una lista de números. El que sí me costó fue el lógico, porque ese ni truena, tuve que comparar la salida que daba contra la que debería dar a mano para darme cuenta que estaba dividiendo entre un número fijo en vez de usar len(lista).

# Compara buscar el bug con print() disperso por el código contra usar el depurador. ¿En qué situación usarías cada uno?
# Yo usaría print() cuando es algo rápido y ya más o menos sé dónde está el problema, nomás para confirmar un valor. El depurador lo usaría cuando el bug es más escondido, como el lógico, porque ahí no basta con ver un valor, hay que ir paso a paso viendo cómo va cambiando todo.

# De los casos que sugirió Copilot, ¿cuántos descartaste? ¿Qué los hacía poco útiles?
# Le pedí que sugiriera casos nuevos para calcular_estadisticas() y sí propuso cosas que no aplicaban tanto, como casos que ya estaban cubiertos con otros que ya tenía en mi tabla. Descarté los que no probaban nada distinto, y me quedé solo con los que sí metían un comportamiento nuevo, como negativos o decimales.

# Compara el programa con el que empezaste esta sesión (bug lógico escondido) contra el que tienes ahora (clasificado, corregido y probado). ¿Qué tan seguro estás de que ya no tiene bugs? ¿Qué te daría más seguridad?
# Pues ya lo veo bastante más sólido, porque ya no solo corrí el código una vez y ya, sino que lo probé con varias listas distintas antes de darlo por bueno. Aun así no digo que esté 100% seguro que no tiene bugs, lo que me daría más seguridad sería meterle más casos límite, como negativos o listas gigantes, y ver que siga dando lo esperado.

# ¿Alguna de tus predicciones en la Actividad 5 falló? ¿Qué operador entendiste distinto de cómo Python lo evalúa?
# No, la verdad todas las prediccioné bien porque fui paso por paso evaluando cada parte antes de juntar el resultado final, como primero ver si 78 < 80 y luego juntar eso con el and o el or. Ya tenía claro que con el and necesito que las dos partes sean verdaderas y con el or basta con una.

# ¿Elegiste if/elif/else o match/case para tu reporte final? ¿Qué criterio de la comparación anterior pesó más en tu decisión?
# Elegí if/elif/else. Lo que más pesó fue que mi clasificación es por rangos de número (90 o más, 80 a 89, etc.), y match/case en Python está más pensado para comparar valores exactos, entonces se sentía forzado tener que ponerle la cláusula extra de "case p if..." para que funcionara con rangos.

# De las 8 actividades de estas dos sesiones, ¿cuál cambió más tu forma de pensar tu código: encontrar un bug lógico, diseñar casos de prueba, o agregar decisiones? ¿Por qué esa?
# Yo creo que diseñar los casos de prueba, porque me hizo pensar en la lista vacía antes de correr nada, y eso fue algo que ni se me hubiera ocurrido si nomás hubiera corrido el código con datos normales. Me hizo ver que probar no es solo correr con datos que sí funcionan, sino buscar los que puedan tronar.

# Compara tu primer programa de la clase de Hello World con reporte_calificaciones.py como está ahora. ¿Qué herramienta (funciones, depurador, pruebas, decisiones) fue la que más cambió cómo escribes código?
# Yo creo que las funciones, porque antes solo escribía todo seguido sin organizarlo, y ahora ya pienso primero en qué le entra, qué hace y qué me regresa. Eso me ayudó a que cuando le agregué las decisiones (if anidados) fuera más fácil de armar, porque ya tenía separado lo que calcula de lo que decide.