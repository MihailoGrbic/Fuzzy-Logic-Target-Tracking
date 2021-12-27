import numpy as np
import pygame

pygame.init()
window = pygame.display.set_mode((0, 0), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN)
# window = pygame.display.set_mode((500, 500), pygame.HWSURFACE | pygame.DOUBLEBUF)

DEFAULT_FONT = 'twcencondensedextra'

colors = {'White': (255, 255, 255),
          'Black': (0, 0, 0),
          'Red': (255, 0, 0),
          'DarkRed': (153, 0, 0),
          'Green': (0, 255, 0),
          'DarkGreen': (0, 153, 0),
          'Blue': (0, 0, 255),
          'DarkBlue': (0, 0, 153),
          'Yellow': (255, 255, 51),
          'DarkYellow': (204, 204, 0),
          'Orange': (255, 153, 51),
          'DarkOrange': (204, 102, 0),
          'Purple': (153, 51, 255),
          'Cyan': (51, 255, 255),
          'DarkCyan': (0, 204, 204),
          }


def quitProgram():
    pygame.quit()
    quit()