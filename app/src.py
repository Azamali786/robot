class Robot:
    """
    A class to represent a robot that can move on a 2D grid.

    Attributes:
        grid_rows : int
            The number of rows in the grid.
        grid_cols : int
            The number of columns in the grid.
        position : tuple
            The current position of the robot in the grid (row, column).
        direction : str
            The direction the robot is currently facing ('N', 'E', 'S', 'W').
        directions : list
            A list of possible directions the robot can face.
        direction_moves : dict
            A dictionary mapping directions to their respective movement vectors.
    """

    def __init__(self, grid_size=(5, 4)):
        """
        Initializes the Robot with a given grid size, initial position, and direction.

        Parameters
        ----------
        grid_size : tuple, optional
            The size of the grid as (rows, columns). Defaults to (5, 4).
        """
        self.grid_rows, self.grid_cols = grid_size
        self.position = (0, 0)
        self.direction = 'S'  # Initial direction is South
        self.directions = ['N', 'E', 'S', 'W']
        self.direction_moves = {
            'N': (-1, 0),  # Move up
            'E': (0, 1),   # Move right
            'S': (1, 0),   # Move down
            'W': (0, -1)   # Move left
        }

    def process_user_command(self, user_command):
        """
        Method to processs user commands in order
        to make it executable
        """
        # remove all spaces from user_command given intentionally or unintentionally
        user_command = user_command.replace(" ", "")

        # convert to Upper Case 
        user_command = user_command.upper()

        return user_command

    def validate_user_command(self, user_command):
        """
        Method to validate given user command
        return:
            (Bool, invalid_values)
        """

        # valid values for the user command
        valid_command_values = {"E", "W", "N", "S", "M", "e", "w", "n", "s", "m", " "}  # Using a set for faster lookup

        # Check for any invalid command
        invalid_values = set(user_command) - valid_command_values

        if invalid_values:
            return (False, invalid_values)
        
        return (True, None)

    def execute_commands(self, commands):
        """
        Executes a sequence of commands to move and/or turn the robot.

        Parameters
        ----------
        commands : str
            A string of commands where each command is either:
            - 'N', 'E', 'S', 'W': Turns the robot to face North, East, South, or West.
            - 'M': Moves the robot one step in the direction it is currently facing.
        """
        
        for command in commands:
            if command in self.directions:
                self.turn(command)
            elif command == 'M':
                self.move()

    
    def turn(self, new_direction):
        """
        Turns the robot to face a new direction.

        Parameters
        ----------
        new_direction : str
            The new direction for the robot to face ('N', 'E', 'S', 'W').
        """
        if self.direction != new_direction:
            self.direction = new_direction
    
    def move(self):
        """
        Moves the robot one step in the direction it is currently facing.
        If the move would take the robot out of the grid bounds, the move is not executed.
        """
        move_row, move_col = self.direction_moves[self.direction]
        new_row = self.position[0] + move_row
        new_col = self.position[1] + move_col
        
        # Check for grid boundaries
        if 0 <= new_row < self.grid_rows and 0 <= new_col < self.grid_cols:
            self.position = (new_row, new_col)
    
    def get_position(self):
        """
        Returns the current position and direction of the robot.

        Returns
        -------
        str
            The robot's position and direction in the format "Robot Location: (row, column, direction)".
        """
        return f"Robot Location: ({self.position[0]}, {self.position[1]}, {self.direction})"
        # return f"Robot Location: {self.position + (self.direction,)}"


if __name__ == "__main__":

    # initialize the robot object
    robot = Robot()

    instructions = """
            Allowed Command Keys : E, W, N, S, e, w, n, s, M, m
            Enter the command to alter the position of robot.
            Enter q or Q to come out of the play.
            Note: 
                1- E, e will change direction or robot to Eastward
                2- W, w will change direction or robot to Westward
                3- N, n will change direction or robot to Northward
                4- S, s will change direction or robot to Southward
                5- M, m will move one step
            """
    print("*" * 80)
    print(instructions)
    print("*" * 80)

    while True:

        # get the COMMAND input from the user
        user_command = input("COMMAND: ")  # Input the command sequence

        if user_command.lower() == "q":
            break

        # validate user_command in order to check against any invalid value in user_command
        valid_user_command, invalid_commands = robot.validate_user_command(user_command)

    
        if valid_user_command:

            # process user command inorder to make it executable
            user_command = robot.process_user_command(user_command)

            # execute give user command
            robot.execute_commands(user_command)

            # get the current position of robot as per given command
            print(robot.get_position())

        else:
            print(f"Invalid value(s) {', '.join(invalid_commands)} found in given COMMAND")

    print("Goodbye!")


        
    

        
