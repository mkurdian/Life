# Life
A non-interactive implementation of Conway's Game of Life using pygame.
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

## Requires
1. Python 3.7.7

## Usage
1. Clone the repository and `cd` into the Life directory.
    ```bash
    git clone https://github.com/mkurdian/Life.git
    cd Life
    ```
1. Create a virtual environment and activate it.
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
1. Install the package:
    ```bash
    pip install .
    ```
1. Run from terminal:
    ```bash
    python -m life.main
    
## Development
1. Follow steps 1 and 2 above.
1. Install the package:
    ```bash
    pip install -e .[tests]
    ```
1. Run tests:
    ```bash
    pytest
    ```

## Screenshot
![Screenshot](screenshot.png)

## Notes
- Confirmed to work on Python version 3.7.7 on Mac OSX 10.15.5.
- Not supported on Python 3.8.x.
- Simulation is not interactive and starts from a random state.