# Robot Movement Simulator

## Overview

This project simulates the movement of a robot on a 2D grid based on a series of commands. 
The robot can move in four directions (North, East, South, West) and can take instructions to move forward or change direction. 
The robot's position and facing direction are tracked and updated as it executes the given commands.

## Features

- **Grid Navigation**: The robot navigates a 5x4 grid (by default), moving within the boundaries based on the commands provided.
- **Directional Control**: The robot can turn to face North (`N`), East (`E`), South (`S`), or West (`W`) or (`n`), East (`e`), South (`s`), or West (`w`)
- **Movement Control**: The robot can move one step forward in the direction it is facing using the `M` or `m` command.
- **Command Validation**: The program checks for any invalid commands and alerts the user if invalid characters are present in the input.
- **User-Friendly**: Input commands are processed to ignore spaces and are case-insensitive.

## Ways to run this code
1. **Using ZIP provided**

    a- Running the robot simulator
    - Unzip the zip robot.zip
    - move inside robot directory
    - run command : python3 -m venv venv                // to make enviroment venv
    - run command : source venv/bin/activate            // to activate environment
    - run command : pip install -r requirements.txt     // to install all dependencies liste din requirements.txt
    - run command : python app/scr.py                   // to run the code of robot simulator
    - entr user command in promt and you will get the current position of robot on console

    b- Running the test cases
    - make sure you are in robot directory where two directories app and test are visible
    - run command : pytest      // this will run the test case





2. **Using Github link provided**
    repo_url = https://github.com/Azamali786/robot.git

    a- runing the robot simulator
    - run command : git clone repo_url   // using above repo url clone the repo
    - move inside robot directory
    - run command : python3 -m venv venv                // to make enviroment venv
    - run command : source venv/bin/activate            // to activate environment
    - run command : pip install -r requirements.txt     // to install all dependencies liste din requirements.txt
    - run command : python app/scr.py                   // to run the code of robot simulator
    - entr user command in promt and you will get the current position of robot on console

    b- Running the test cases
    - make sure you are in robot directory where two directories app and test are visible
    - run command : pytest      // this will run the test case



## Notes
1. **Ensure you have Python 3.x installed**:
    - You can check your Python version by running:
      ```bash
      python --version
      ```
    - If you don’t have Python installed, download it from [python.org](https://www.python.org/downloads/)

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

