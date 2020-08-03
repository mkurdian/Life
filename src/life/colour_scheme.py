from dataclasses import dataclass
from typing import Tuple


@dataclass
class ColourScheme:
    """
    A class to take the responsibility of the colours used for each aspect of the
    life rendering.
    """
    grid: Tuple
    background: Tuple
    live_cell: Tuple
    dead_cell: Tuple

    # Colour scheme colours
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
