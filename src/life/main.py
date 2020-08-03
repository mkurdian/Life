import sys

import pygame

from life.colour_scheme import ColourScheme
from life.life_sim import Life
from life.life_drawer import LifeDrawer


def main():
    pygame.init()
    pygame.display.set_caption("Conway's Game Of Life")

    colour_scheme = ColourScheme(grid=ColourScheme.BLACK,
                                 background=ColourScheme.WHITE,
                                 live_cell=ColourScheme.BLUE,
                                 dead_cell=ColourScheme.WHITE)

    window = pygame.display.set_mode((500, 500))

    life = Life(rows=50, cols=50)
    life.load_random()

    life_drawer = LifeDrawer(surface=window,
                             colour_scheme=colour_scheme,
                             life_obj=life)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        life.update()
        life_drawer.update()


if __name__ == '__main__':
    main()

