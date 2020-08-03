from enum import Enum, auto


class CellState(Enum):
    """
    An enum representation of the cell state.
    """
    Alive = auto()
    Dead = auto()
