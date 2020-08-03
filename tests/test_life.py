from pytest import fixture

from life.cell_state import CellState
from life.life_sim import Life


@fixture
def life_5_by_5():
    return Life(5, 5)


def test_load_random(life_5_by_5):
    life_5_by_5.load_random()

    # Count number of cells in grid.
    count = 0
    for _ in life_5_by_5.grid_cells():
        count += 1

    assert count == 25


def test_load_glider(life_5_by_5):
    life_5_by_5.load_glider()

    # Count number of cells in grid.
    count = 0
    for _ in life_5_by_5.grid_cells():
        count += 1

    assert count == 25

    # Assert starting configuration of glider pattern:
    # First row
    assert life_5_by_5.grid_cell(0, 0).state is CellState.Dead
    assert life_5_by_5.grid_cell(0, 1).state is CellState.Dead
    assert life_5_by_5.grid_cell(0, 2).state is CellState.Dead
    assert life_5_by_5.grid_cell(0, 3).state is CellState.Dead
    assert life_5_by_5.grid_cell(0, 4).state is CellState.Dead
    # Second row
    assert life_5_by_5.grid_cell(1, 0).state is CellState.Dead
    assert life_5_by_5.grid_cell(1, 1).state is CellState.Dead
    assert life_5_by_5.grid_cell(1, 2).state is CellState.Alive
    assert life_5_by_5.grid_cell(1, 3).state is CellState.Dead
    assert life_5_by_5.grid_cell(1, 4).state is CellState.Dead
    # Third row
    assert life_5_by_5.grid_cell(2, 0).state is CellState.Dead
    assert life_5_by_5.grid_cell(2, 1).state is CellState.Dead
    assert life_5_by_5.grid_cell(2, 2).state is CellState.Dead
    assert life_5_by_5.grid_cell(2, 3).state is CellState.Alive
    assert life_5_by_5.grid_cell(2, 4).state is CellState.Dead
    # Fourth row
    assert life_5_by_5.grid_cell(3, 0).state is CellState.Dead
    assert life_5_by_5.grid_cell(3, 1).state is CellState.Alive
    assert life_5_by_5.grid_cell(3, 2).state is CellState.Alive
    assert life_5_by_5.grid_cell(3, 3).state is CellState.Alive
    assert life_5_by_5.grid_cell(3, 4).state is CellState.Dead
    # Fifth row
    assert life_5_by_5.grid_cell(4, 0).state is CellState.Dead
    assert life_5_by_5.grid_cell(4, 1).state is CellState.Dead
    assert life_5_by_5.grid_cell(4, 2).state is CellState.Dead
    assert life_5_by_5.grid_cell(4, 3).state is CellState.Dead
    assert life_5_by_5.grid_cell(4, 4).state is CellState.Dead


def test_update(life_5_by_5):

    life_5_by_5.load_glider()
    life_5_by_5.update()

    # Assert first update of glider:
    # First row
    assert life_5_by_5.grid_cell(0, 0).state is CellState.Dead
    assert life_5_by_5.grid_cell(0, 1).state is CellState.Dead
    assert life_5_by_5.grid_cell(0, 2).state is CellState.Dead
    assert life_5_by_5.grid_cell(0, 3).state is CellState.Dead
    assert life_5_by_5.grid_cell(0, 4).state is CellState.Dead
    # Second row
    assert life_5_by_5.grid_cell(1, 0).state is CellState.Dead
    assert life_5_by_5.grid_cell(1, 1).state is CellState.Dead
    assert life_5_by_5.grid_cell(1, 2).state is CellState.Dead
    assert life_5_by_5.grid_cell(1, 3).state is CellState.Dead
    assert life_5_by_5.grid_cell(1, 4).state is CellState.Dead
    # Third row
    assert life_5_by_5.grid_cell(2, 0).state is CellState.Dead
    assert life_5_by_5.grid_cell(2, 1).state is CellState.Alive
    assert life_5_by_5.grid_cell(2, 2).state is CellState.Dead
    assert life_5_by_5.grid_cell(2, 3).state is CellState.Alive
    assert life_5_by_5.grid_cell(2, 4).state is CellState.Dead
    # Fourth row
    assert life_5_by_5.grid_cell(3, 0).state is CellState.Dead
    assert life_5_by_5.grid_cell(3, 1).state is CellState.Dead
    assert life_5_by_5.grid_cell(3, 2).state is CellState.Alive
    assert life_5_by_5.grid_cell(3, 3).state is CellState.Alive
    assert life_5_by_5.grid_cell(3, 4).state is CellState.Dead
    # Fifth row
    assert life_5_by_5.grid_cell(4, 0).state is CellState.Dead
    assert life_5_by_5.grid_cell(4, 1).state is CellState.Dead
    assert life_5_by_5.grid_cell(4, 2).state is CellState.Alive
    assert life_5_by_5.grid_cell(4, 3).state is CellState.Dead
    assert life_5_by_5.grid_cell(4, 4).state is CellState.Dead
