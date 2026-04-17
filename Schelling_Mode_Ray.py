import pygame
import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
#matplotlib inline
 

N = 400                   # Tamaño de la grilla rectangular de N x N
Si = 0.75                 # Factor de satisfacción, S = 1-tolerance
f_vac = 0.1               # Fracción de sitios vacantes
Nv = int(N*N*f_vac)       # Número de sitios vacantes
Na = N*N-Nv               # Número de agentes en la simulación
f_red = 0.15               # Fracción de agentes rojos
f_blue = 1-f_red          # Fracción de agentes azules

def Initial_state(N:int, Nv:int, Na:int, f_red:float):
    """
    Initial_state crea un grilla rectangulas de N x N, de manera que:
    Blue  =  0
    Red   =  1
    Vacante = -1

    :param N: tamaño de la grilla de NxN
    :param Nv: números de sitios vacantes 
    :param Na: número de agentes
    :param f_red: fracción de agentes rojos
    :return: autómata celular en la generación 0
    """
    reds = int(Na*f_red)
    grid = np.zeros(N*N)
    grid[:reds] = 1
    grid[-Nv:] = -1
    np.random.shuffle(grid)
    return grid.reshape(N,N)

grid = Initial_state(N,Nv,Na,f_red)

def Schelling_rules(grid):
    
    KERNEL = np.array([[1, 1, 1],
                   [1, 0, 1],
                   [1, 1, 1]])
    
    # Tenemos que contar los vecinos por cada color (blue = 0, red = 1) y los
    # vecinos totales por cada célula dependiendo del color
    blue_counts = convolve2d(grid == 0, KERNEL, mode='same', boundary='wrap')
    red_counts = convolve2d(grid == 1, KERNEL, mode='same', boundary='wrap')
    
    # contamos los vecinos alrededor de cada célula que no sean sitios vacantes
    neighbor_count  = convolve2d(grid != -1,  KERNEL, mode='same', boundary='wrap')
    
    # Ahora vamos a cuantificar el grado de insatisfacción por cada color 
    # Para ello, vamos a contar la fracción de sitios azules y si esa fracción
    # es menor que el grado de satisfacción, entonces generemos un 1, en caso contrario un 0
    blue_dissatified = (blue_counts/neighbor_count < Si) & (grid == 0)
    red_dissatified = (red_counts/neighbor_count < Si) & (grid == 1)
    
    # Todos los sitios insatisfechos los cambiamos de estado, y pasan a estar vacios (-1)
    grid[red_dissatified | blue_dissatified] = - 1
    
    # Ahora contamos cuantos sitios vacantes tenemos disponibles para mover los agentes insatisfechos
    vacancy = (grid == -1).sum()
    
    # Contamos cuantos agentes azules y rojos tenemos insatisfechos
    n_b_dissatified, n_r_dissatified = blue_dissatified.sum(), red_dissatified.sum()
    
    # Creamos un arreglo unidimensional con valores -1 y cuya dimensión es igual al número de sitios 
    # vacantes
    filling = -np.ones(vacancy) 
    
    # Los primeros valores del arreglo se llenan con 0 (agentes azules)
    filling[:n_b_dissatified] = 0
    
    # El resto de los valores del arreglo se llenan con +1 (agentes rojos)
    filling[n_b_dissatified:n_b_dissatified + n_r_dissatified] = 1
    
    # Ahora reordenamos de forma aleatoria el arreglo que contiene -1, 0 y +1
    np.random.shuffle(filling)
    
    # Finalmente llenamos los sitios de la grilla que están vacios usando el arreglo filling
    # esta parte corresponde a mover los agentes insatisfechos
    grid[grid==-1] = filling
    
    return grid

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
cell_size = 2
width, height = N * cell_size, N * cell_size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Schelling model")


# Bucle principal
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Aplicar las reglas del juego de la vida
    grid = Schelling_rules(grid)

    # Dibujar el estado actual del juego
    screen.fill((0, 0, 0))
    for y in range(N):
        for x in range(N):
            color = (0, 0, 255) if grid[y, x] == 0 else \
            (255, 0, 0) if grid[y, x] == 1 else \
            (250, 250, 250)
            pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))

    pygame.display.flip()
    clock.tick(5)  # Controla la velocidad de la animación ajustando este valor

# Finalizar Pygame
pygame.quit()