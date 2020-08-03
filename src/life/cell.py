from life.cell_state import CellState


class Cell:
    """
    A representation of a grid cell.
    """
    def __init__(self, row: int, col: int, state: CellState):
        """
        Constructor.

        :param row: Row 0-based index.
        :param col: Column 0-based index.
        :param state: Initial state of cell.
        """
        self.row = row
        self.col = col
        self.state = state
