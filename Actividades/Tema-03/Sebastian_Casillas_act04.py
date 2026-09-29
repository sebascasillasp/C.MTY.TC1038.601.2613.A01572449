# Sebastián Casillas Portillo
# A01572449
# Librerías para la actividad

import pyfiglet
print(pyfiglet.figlet_format("Actividad 3", font="slant"))

"""
Pac-Man - juego con pygame
Sebastián Casillas Portillo

Controles:
  Flechas del teclado -> mover a Pac-Man
  ESC -> salir
  R -> reiniciar (cuando ganas o pierdes)

Objetivo: come todos los puntos sin que te atrape un fantasma.
Las "power pellets" (bolitas grandes) te dejan comer fantasmas por unos segundos.
"""

import pygame
import random
import sys

# ---------- Configuración ----------
TAM = 24  # tamaño de celda en píxeles
FPS = 60

# 0 = pared, 1 = punto normal, 2 = vacío (pasillo sin punto), 3 = power pellet
MAPA = [
    "00000000000000000000000",
    "03110111111111111111130",
    "00010101010101010101000",
    "01111101010101011101110",
    "01010101010101000100010",
    "01011101110101011111010",
    "01010001010100010001010",
    "01011111010111010111010",
    "01000100010001010101010",
    "11111111111101110101011",
    "01010101010101010101010",
    "01111111111101110111010",
    "01010000000100000101010",
    "01111111111111111111110",
    "01000100010001010001010",
    "01110111111111011111110",
    "01010000010101010000000",
    "03111111111111111111130",
    "00000000000000000000000",
]

FILAS = len(MAPA)
COLUMNAS = len(MAPA[0])
ANCHO = COLUMNAS * TAM
ALTO = FILAS * TAM + 60  # espacio extra para el HUD

# Colores
NEGRO = (0, 0, 0)
AZUL = (33, 33, 222)
AMARILLO = (255, 220, 0)
BLANCO = (245, 245, 245)
ROJO = (220, 40, 40)
ROSA = (255, 150, 200)
CYAN = (60, 220, 220)
NARANJA = (240, 150, 40)
AZUL_MIEDO = (40, 40, 220)

pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pac-Man - Sebastián Casillas")
reloj = pygame.time.Clock()
fuente = pygame.font.SysFont("Arial", 26, bold=True)
fuente_chica = pygame.font.SysFont("Arial", 18)

DIRECCIONES = {
    pygame.K_UP: (0, -1),
    pygame.K_w: (0, -1),
    pygame.K_DOWN: (0, 1),
    pygame.K_s: (0, 1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_a: (-1, 0),
    pygame.K_RIGHT: (1, 0),
    pygame.K_d: (1, 0),
}


def es_pared(col, fila):
    if fila < 0 or fila >= FILAS or col < 0 or col >= COLUMNAS:
        return True
    return MAPA[fila][col] == "0"


def crear_grid_puntos():
    """Regresa un set con (col, fila) de puntos normales y otro de power pellets."""
    puntos = set()
    power = set()
    for f, fila in enumerate(MAPA):
        for c, celda in enumerate(fila):
            if celda == "1":
                puntos.add((c, f))
            elif celda == "3":
                power.add((c, f))
    return puntos, power


class Personaje:
    def __init__(self, col, fila, color):
        self.col = col
        self.fila = fila
        self.color = color
        self.dir = (0, 0)
        self.dir_deseada = (0, 0)
        self.progreso = 0.0  # de 0 a 1, avance hacia la siguiente celda

    @property
    def px(self):
        return (self.col + self.dir[0] * self.progreso) * TAM + TAM / 2

    @property
    def py(self):
        return (self.fila + self.dir[1] * self.progreso) * TAM + TAM / 2 + 60


def puede_moverse(col, fila, direccion):
    nc, nf = col + direccion[0], fila + direccion[1]
    return not es_pared(nc, nf)


def avanzar(personaje, velocidad):
    """Mueve al personaje celda por celda con interpolación suave."""
    if personaje.dir == (0, 0) and personaje.dir_deseada == (0, 0):
        return

    # Reversa inmediata: si el jugador pide la dirección contraria a mitad de
    # camino entre dos celdas, date la vuelta al instante (sin teletransportar
    # visualmente) en vez de esperar a llegar a la siguiente celda.
    if personaje.dir != (0, 0) and personaje.dir_deseada == (-personaje.dir[0], -personaje.dir[1]):
        personaje.col = (personaje.col + personaje.dir[0]) % COLUMNAS
        personaje.fila = max(0, min(FILAS - 1, personaje.fila + personaje.dir[1]))
        personaje.progreso = 1.0 - personaje.progreso
        personaje.dir = personaje.dir_deseada

    # Si no se está moviendo, intenta arrancar en la dirección deseada
    if personaje.progreso == 0.0:
        if personaje.dir_deseada != (0, 0) and puede_moverse(personaje.col, personaje.fila, personaje.dir_deseada):
            personaje.dir = personaje.dir_deseada
        if personaje.dir != (0, 0) and not puede_moverse(personaje.col, personaje.fila, personaje.dir):
            personaje.dir = (0, 0)
            return

    if personaje.dir == (0, 0):
        return

    personaje.progreso += velocidad
    if personaje.progreso >= 1.0:
        personaje.progreso = 0.0
        personaje.col = (personaje.col + personaje.dir[0]) % COLUMNAS
        personaje.fila = personaje.fila + personaje.dir[1]
        # permitir túnel horizontal si algún día se agrega; por ahora solo columnas
        if personaje.fila < 0:
            personaje.fila = 0
        if personaje.fila >= FILAS:
            personaje.fila = FILAS - 1

        # intenta girar hacia la dirección deseada al llegar a la celda
        if personaje.dir_deseada != (0, 0) and puede_moverse(personaje.col, personaje.fila, personaje.dir_deseada):
            personaje.dir = personaje.dir_deseada
        elif not puede_moverse(personaje.col, personaje.fila, personaje.dir):
            personaje.dir = (0, 0)


def mover_fantasma_ia(fantasma, pacman, asustado):
    """IA simple: en cada intersección elige la dirección que más acerca (o aleja) a Pac-Man."""
    if fantasma.progreso != 0.0:
        avanzar(fantasma, fantasma.velocidad)
        return

    opciones = []
    for d in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        # evita que se devuelva por donde vino, salvo que no haya otra opción
        if d == (-fantasma.dir[0], -fantasma.dir[1]) and fantasma.dir != (0, 0):
            continue
        if puede_moverse(fantasma.col, fantasma.fila, d):
            opciones.append(d)

    if not opciones:
        opciones = [d for d in [(0, -1), (0, 1), (-1, 0), (1, 0)] if puede_moverse(fantasma.col, fantasma.fila, d)]

    if opciones:
        if asustado:
            # huye: elige la dirección que maximiza distancia a Pac-Man
            mejor = max(
                opciones,
                key=lambda d: (fantasma.col + d[0] - pacman.col) ** 2 + (fantasma.fila + d[1] - pacman.fila) ** 2,
            )
        else:
            mejor = min(
                opciones,
                key=lambda d: (fantasma.col + d[0] - pacman.col) ** 2 + (fantasma.fila + d[1] - pacman.fila) ** 2,
            )
        # un poco de aleatoriedad para que no sean perfectos
        if random.random() < 0.2:
            mejor = random.choice(opciones)
        fantasma.dir_deseada = mejor
        fantasma.dir = mejor

    avanzar(fantasma, fantasma.velocidad)


def dibujar_mapa():
    for f in range(FILAS):
        for c in range(COLUMNAS):
            x, y = c * TAM, f * TAM + 60
            if es_pared(c, f):
                pygame.draw.rect(pantalla, AZUL, (x, y, TAM, TAM))
                pygame.draw.rect(pantalla, NEGRO, (x, y, TAM, TAM), 1)


def dibujar_puntos(puntos, power):
    for (c, f) in puntos:
        cx, cy = c * TAM + TAM // 2, f * TAM + TAM // 2 + 60
        pygame.draw.circle(pantalla, BLANCO, (cx, cy), 3)
    for (c, f) in power:
        cx, cy = c * TAM + TAM // 2, f * TAM + TAM // 2 + 60
        pygame.draw.circle(pantalla, AMARILLO, (cx, cy), 7)


def dibujar_pacman(pac, boca_abierta):
    x, y = int(pac.px), int(pac.py)
    r = TAM // 2 - 2
    ang_map = {(1, 0): 0, (-1, 0): 180, (0, -1): 90, (0, 1): 270, (0, 0): 0}
    base = ang_map.get(pac.dir, 0)
    if boca_abierta:
        pygame.draw.circle(pantalla, AMARILLO, (x, y), r)
        # "boca" como un triángulo negro
        import math
        a1 = math.radians(base + 30)
        a2 = math.radians(base - 30)
        p1 = (x, y)
        p2 = (x + r * math.cos(a1), y - r * math.sin(a1))
        p3 = (x + r * math.cos(a2), y - r * math.sin(a2))
        pygame.draw.polygon(pantalla, NEGRO, [p1, p2, p3])
    else:
        pygame.draw.circle(pantalla, AMARILLO, (x, y), r)


def dibujar_fantasma(f, asustado):
    x, y = int(f.px), int(f.py)
    r = TAM // 2 - 2
    color = AZUL_MIEDO if asustado else f.color
    pygame.draw.circle(pantalla, color, (x, y - 2), r)
    pygame.draw.rect(pantalla, color, (x - r, y - 2, r * 2, r + 2))
    # ojos
    if not asustado:
        pygame.draw.circle(pantalla, BLANCO, (x - 5, y - 4), 4)
        pygame.draw.circle(pantalla, BLANCO, (x + 5, y - 4), 4)
        pygame.draw.circle(pantalla, NEGRO, (x - 5, y - 4), 2)
        pygame.draw.circle(pantalla, NEGRO, (x + 5, y - 4), 2)


def mostrar_texto_centrado(texto, y, color=BLANCO, fnt=None):
    fnt = fnt or fuente
    render = fnt.render(texto, True, color)
    rect = render.get_rect(center=(ANCHO // 2, y))
    pantalla.blit(render, rect)


def primer_celda_libre():
    """Recorre el mapa y regresa la primera celda que no sea pared (respaldo de seguridad)."""
    for f in range(FILAS):
        for c in range(COLUMNAS):
            if not es_pared(c, f):
                return (c, f)
    return (0, 0)


def celda_libre_inicial(candidatas):
    for c in candidatas:
        if not es_pared(*c):
            return c
    return primer_celda_libre()


PACMAN_SPAWN = (11, 9)  # celda abierta cerca del centro del laberinto (verificada)
FANTASMA_SPAWNS = [(1, 1), (21, 1), (1, 17), (21, 17)]  # las 4 esquinas, verificadas abiertas
INVULNERABILIDAD_MS = 2000


def crear_estado_inicial():
    """Crea (o reinicia) todo el estado del juego en un solo diccionario."""
    puntos, power = crear_grid_puntos()

    pacman = Personaje(*celda_libre_inicial([PACMAN_SPAWN]), AMARILLO)
    pacman.velocidad = 0.10

    colores_fantasmas = [ROJO, ROSA, CYAN, NARANJA]
    fantasmas = []
    for pos, color in zip(FANTASMA_SPAWNS, colores_fantasmas):
        f = Personaje(*celda_libre_inicial([pos]), color)
        f.velocidad = 0.08
        fantasmas.append(f)

    return {
        "puntos": puntos,
        "power": power,
        "pacman": pacman,
        "fantasmas": fantasmas,
        "puntaje": 0,
        "vidas": 3,
        "estado": "jugando",  # jugando, ganaste, perdiste
        "modo_asustado_ms": 0,
        "invulnerable_ms": 0,
    }


def reposicionar_fantasmas(fantasmas):
    for f, pos in zip(fantasmas, FANTASMA_SPAWNS):
        f.col, f.fila = celda_libre_inicial([pos])
        f.progreso = 0.0
        f.dir = (0, 0)
        f.dir_deseada = (0, 0)


def main():
    juego = crear_estado_inicial()
    tick_boca = 0

    corriendo = True
    while corriendo:
        dt = reloj.tick(FPS)
        tick_boca += dt
        boca_abierta = (tick_boca // 150) % 2 == 0

        pacman = juego["pacman"]
        fantasmas = juego["fantasmas"]
        puntos = juego["puntos"]
        power = juego["power"]

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    corriendo = False
                elif evento.key in DIRECCIONES and juego["estado"] == "jugando":
                    pacman.dir_deseada = DIRECCIONES[evento.key]
                elif evento.key == pygame.K_r and juego["estado"] != "jugando":
                    juego = crear_estado_inicial()
                    tick_boca = 0
                    pacman = juego["pacman"]
                    fantasmas = juego["fantasmas"]
                    puntos = juego["puntos"]
                    power = juego["power"]

        if juego["estado"] == "jugando":
            if juego["invulnerable_ms"] > 0:
                juego["invulnerable_ms"] -= dt

            avanzar(pacman, pacman.velocidad)

            asustado = juego["modo_asustado_ms"] > 0
            if asustado:
                juego["modo_asustado_ms"] -= dt

            for f in fantasmas:
                mover_fantasma_ia(f, pacman, asustado)

            pos_pac = (pacman.col, pacman.fila)
            if pos_pac in puntos:
                puntos.discard(pos_pac)
                juego["puntaje"] += 10
            if pos_pac in power:
                power.discard(pos_pac)
                juego["puntaje"] += 50
                juego["modo_asustado_ms"] = 6000  # 6 segundos de poder

            # colisiones con fantasmas (ignoradas durante la invulnerabilidad)
            if juego["invulnerable_ms"] <= 0:
                for f in fantasmas:
                    if f.col == pacman.col and f.fila == pacman.fila:
                        if juego["modo_asustado_ms"] > 0:
                            juego["puntaje"] += 200
                            f.col, f.fila = celda_libre_inicial([PACMAN_SPAWN])
                            f.progreso = 0.0
                            f.dir = (0, 0)
                        else:
                            juego["vidas"] -= 1
                            if juego["vidas"] <= 0:
                                juego["estado"] = "perdiste"
                            else:
                                pacman.col, pacman.fila = celda_libre_inicial([PACMAN_SPAWN])
                                pacman.progreso = 0.0
                                pacman.dir = (0, 0)
                                pacman.dir_deseada = (0, 0)
                                reposicionar_fantasmas(fantasmas)
                                juego["invulnerable_ms"] = INVULNERABILIDAD_MS
                            break  # solo procesa un golpe por frame

            if len(puntos) + len(power) == 0:
                juego["estado"] = "ganaste"

        # ---------- Dibujo ----------
        pantalla.fill(NEGRO)
        dibujar_mapa()
        dibujar_puntos(puntos, power)

        # Pac-Man parpadea mientras es invulnerable, para que se note
        dibujar_pac = juego["invulnerable_ms"] <= 0 or (tick_boca // 100) % 2 == 0
        if dibujar_pac:
            dibujar_pacman(pacman, boca_abierta)
        for f in fantasmas:
            dibujar_fantasma(f, juego["modo_asustado_ms"] > 0)

        texto_puntaje = fuente.render(f"Puntaje: {juego['puntaje']}", True, BLANCO)
        pantalla.blit(texto_puntaje, (10, 15))
        texto_vidas = fuente.render(f"Vidas: {juego['vidas']}", True, BLANCO)
        pantalla.blit(texto_vidas, (ANCHO - 150, 15))

        # Aviso breve al inicio: si no le has dado clic a la ventana, el teclado no responde
        if tick_boca < 4000 and juego["estado"] == "jugando":
            aviso = fuente_chica.render("Haz clic en esta ventana para activarla", True, AMARILLO)
            rect_aviso = aviso.get_rect(center=(ANCHO // 2, ALTO - 12))
            pantalla.blit(aviso, rect_aviso)

        if juego["estado"] != "jugando":
            overlay = pygame.Surface((ANCHO, ALTO), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 170))
            pantalla.blit(overlay, (0, 0))
            if juego["estado"] == "ganaste":
                mostrar_texto_centrado("¡Ganaste! 🎉", ALTO // 2 - 30, AMARILLO)
            else:
                mostrar_texto_centrado("Game Over 💀", ALTO // 2 - 30, ROJO)
            mostrar_texto_centrado(f"Puntaje final: {juego['puntaje']}", ALTO // 2 + 10, BLANCO)
            mostrar_texto_centrado("Presiona R para reiniciar", ALTO // 2 + 50, CYAN, fuente_chica)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()