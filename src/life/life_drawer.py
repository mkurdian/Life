import pygame

from life.cell_state import CellState
from life.colour_scheme import ColourScheme
from life.life_sim import Life


class LifeDrawer:
    """
    A class to take responsibility of rendering the life simulation on the screen.
    """
    def __init__(self, surface: pygame.Surface, colour_scheme: ColourScheme, life_obj: Life):
        """
        Constructor.

        :param surface: The pygame window onto which to render.
        :param colour_scheme: Colour scheme object to set the render colours.
        :param life_obj: The Life simulation object to represent onto the window.
        """
        self.surface = surface
        self.colour_scheme = colour_scheme
        self.life_obj = life_obj

    @property
    def get_cell_width(self) -> int:
        """
        The cell width to be displayed on the screen in pixels.

        :return: Cell width in pixels.
        """
        return self.surface.get_width() // self.life_obj.cols

    @ property
    def get_cell_height(self) -> int:
        """
        The cell height to be displayed on the screen in pixels.

        :return: Cell height in pixels.
        """
        return self.surface.get_height() // self.life_obj.rows

    def draw_grid(self) -> None:
        """
        Draws the representation of grid pattern onto the screen.
        """
        for row in range(1, self.life_obj.rows):
            start_position = (0, row * self.get_cell_height)
            end_position = (self.surface.get_width(), row * self.get_cell_height)
            pygame.draw.line(self.surface, self.colour_scheme.grid, start_position, end_position)

        for col in range(1, self.life_obj.cols):
            start_position = (col * self.get_cell_width, 0)
            end_position = (col * self.get_cell_width, self.surface.get_height())
            pygame.draw.line(self.surface, self.colour_scheme.grid, start_position, end_position)

    def draw_cell(self, rgb_colour, row: int, col: int) -> None:
        """
        Draws a rectangle with given row and column coordinates onto the screen.

        :param rgb_colour: Colour of cell.
        :param row: Row 0-based index of cell.
        :param col: Column 0-based index of Cell.
        """
        x_pos = row * self.get_cell_width
        y_pos = col * self.get_cell_height
        pygame.draw.rect(self.surface, rgb_colour, (x_pos, y_pos, self.get_cell_width, self.get_cell_height))

    def draw_cells(self) -> None:
        """
        Draws the representation of the alive and dead cells onto the screen.
        """
        for cell in self.life_obj.grid_cells():
            if cell.state is CellState.Alive:
                self.draw_cell(self.colour_scheme.live_cell, cell.col, cell.row)
            elif cell.state is CellState.Dead:
                self.draw_cell(self.colour_scheme.dead_cell, cell.col, cell.row)

    def update(self) -> None:
        """
        Refreshes the screen.
        """
        self.draw_cells()
        self.draw_grid()
        pygame.display.update()

