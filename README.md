# Robot Movement Simulator

## Overview

This project simulates the movement of a robot on a 2D grid based on a series of commands. 
The robot can move in four directions (North, East, South, West) and can take instructions to move forward or change direction. 
The robot's position and facing direction are tracked and updated as it executes the given commands.

## Features

- **Grid Navigation**: The robot navigates a 5x4 grid (by default), moving within the boundaries based on the commands provided.
- **Directional Control**: The robot can turn to face North (`N`), East (`E`), South (`S`), or West (`W`).
- **Movement Control**: The robot can move one step forward in the direction it is facing using the `M` command.
- **Command Validation**: The program checks for any invalid commands and alerts the user if invalid characters are present in the input.
- **User-Friendly**: Input commands are processed to ignore spaces and are case-insensitive.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/robot-movement-simulator.git
    cd robot-movement-simulator
    ```

2. **Ensure you have Python 3.x installed**:
    - You can check your Python version by running:
      ```bash
      python --version
      ```
    - If you don’t have Python installed, download it from [python.org](https://www.python.org/downloads/).

3. **Install pytest for testing** (if not already installed):
    ```bash
    pip install pytest
    ```

## Usage

To use the Robot Movement Simulator:

1. **Run the Program**:
    ```bash
    python robot.py
    ```

2. **Input Commands**:
    - Enter a sequence of commands consisting of:
      - `N`: Turn North
      - `E`: Turn East
      - `S`: Turn South
      - `W`: Turn West
      - `M`: Move forward in the current direction
    - Example: `MSMMEMM`
    - The robot will execute these commands and display its final position and facing direction.

3. **Quit the Program**:
    - Enter `q` to exit the program.

4. **Command Validation**:
    - If the command contains invalid characters (e.g., `X`, `!`, `#`), the program will notify you and reject the command.

## Example Interaction

```plaintext
$ python robot.py
COMMAND: MSMMEMM
Robot Location: (3, 2, E)

COMMAND: q
Goodbye!
