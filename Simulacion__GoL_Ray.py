import pygame
import numpy as np
from scipy.signal import convolve2d

# FUNCIÓN PARA APLICAR LAS REGLAS DEL JUEGO DE LA VIDA

def GoL_rules(grid):
    kernel = np.array([[1,1,1],
                       [1,1,1],
                       [1,1,1]])
    conteo_vecinos = convolve2d(grid,kernel, mode = "same", boundary = "fill")
    return (conteo_vecinos == 3) + ((conteo_vecinos == 4) & grid)


# TAMAÑO DEL MUNDO Y ESTADO DEL AC_0 (GENERACIÓN 0)

N = 300
grid = np.random.randint(2, size = (N,N))



# CREAMOS EL ENTORNO PYGAME PARA VISUALIZAR EL JUEGO

pygame.init() 

# Configuracion de la ventana

tam_celda = 4
width, height = N * tam_celda, N * tam_celda
pantalla = pygame.display.set_mode((width, height))
pygame.display.set_caption("Conway's Game of Life")

# BUCLE INFINITO PARA SIMULACIÓN

# Bucle principal
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Aplicar las reglas del juego de la vida
    grid = GoL_rules(grid)

    # Dibujar el estado actual del juego
    pantalla.fill((0, 0, 0))
    for y in range(N):
        for x in range(N):
            color = (255, 255, 255) if grid[y, x] == 1 else (0, 0, 0)
            pygame.draw.rect(pantalla, color, (x * tam_celda, y * tam_celda, tam_celda, tam_celda))

    pygame.display.flip()
    clock.tick(10)  # Controla la velocidad de la animación ajustando este valor

# Finalizar Pygame
pygame.quit()
