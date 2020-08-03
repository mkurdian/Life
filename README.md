# Life
A non-interactive implementation of Conway's Game of Life using pygame.
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

## Usage
1. With activated virtual environment run the following inside the Life directory
to be able to run the tests:
    ```bash
    pip install -e .[tests]
    ```
1. Run tests:
    ```bash
    pytest
    ```
1. Run from terminal:
    ```bash
    python -m life.main
    ```

## Screenshot
![Screenshot](screenshot.png)

## Notes
- Only confirmed to work on Python version 3.7.7.
- Simulation is not interactive and starts from a random state.