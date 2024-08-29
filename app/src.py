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

    

        
    

        
