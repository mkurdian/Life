import random
from typing import Iterator, Iterable

from life.cell import Cell
from life.cell_state import CellState


class Life:
    """
    A representation of Conway's game of life simulation.
    """
    def __init__(self, rows: int, cols: int):
        """
        Constructor.

        :param rows: The number of rows in the 2d grid.
        :param cols: The number of columns in the 2d grid.
        """
        self.rows = rows
        self.cols = cols
        self.grid_2d = None
        self.initialise()

    def initialise(self):
        """
        Initialise the contents of the 2d grid with default dead cells.
        """
        self.grid_2d = list()
        for row in range(self.rows):
            new_row = []
            for col in range(self.cols):
                new_row.append(Cell(row, col, CellState.Dead))
            self.grid_2d.append(new_row)

    def load_glider(self):
        """
        Loads the 2d grid with the glider pattern.
        """
        glider_positions = [(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
        for position in glider_positions:
            self.grid_cell(*position).state = CellState.Alive

    def load_random(self):
        """
        Loads the 2d grid with a random distribution of live
        and dead cells.
        """
        for cell in self.grid_cells():
            cell.state = random .choice([CellState.Alive, CellState.Dead])

    def grid_cells(self) -> Iterator:
        """
        Returns all of the cells in the 2d grid as an iterator.

        :return: Iterator of grid cells in the 2d grid.
        """
        for row in self.grid_2d:
            for cell in row:
                yield cell

    def grid_cell(self, row: int, col: int) -> Cell:
        """
        Returns the cell from the 2d grid for the given
        row and column indexes.

        :param row: Row 0-based index.
        :param col: Column 0-based index.
        :return: Grid cell corresponding for give row and column index.
        """
        if row < 0:
            row = row % self.rows + self.rows
        if row >= self.rows:
            row %= self.rows
        if col < 0:
            col = col % self.cols + self.cols
        if col >= self.cols:
            col %= self.cols
        return self.grid_2d[row][col]

    def get_live_neighbours(self, cell: Cell) -> Iterable:
        """
        Returns live neighbours of given cell.
        Repeating boundary conditions are used.

        :param cell: Cell to obtain live neighbours for.
        :return: Iterable of live neighbours.
        """
        row, col = cell.row, cell.col
        neighbours = list()
        neighbour_positions = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),  # row above cell
                               (row, col - 1), (row, col + 1),                          # same row as cell
                               (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]  # row below cell

        for position in neighbour_positions:
            neighbours.append(self.grid_cell(*position))

        return [neighbour for neighbour in neighbours if neighbour.state == CellState.Alive]

    def update(self):
        """
        Update the cells in the grid according to the following rules:
        1. Any live cell with two or three live neighbours survives.
        2. Any dead cell with three live neighbours becomes a live cell.
        3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.

        https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Rules
        """
        next_state = dict()

        # Obtain value for the next state of each cell.
        for cell in self.grid_cells():
            live_neighbour_count = len(self.get_live_neighbours(cell))

            if cell.state is CellState.Alive and live_neighbour_count in [2, 3]:
                next_state[cell] = CellState.Alive
            elif cell.state is CellState.Dead and live_neighbour_count == 3:
                next_state[cell] = CellState.Alive
            else:
                next_state[cell] = CellState.Dead

        # Replace current state with next state.
        for cell in self.grid_cells():
            cell.state = next_state[cell]








