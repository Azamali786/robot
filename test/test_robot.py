import pytest
from app.src import Robot

@pytest.fixture
def robot():
    """Fixture to create a Robot instance for testing."""
    return Robot()

def test_initial_position(robot):
    """Test the initial position and direction of the robot."""
    assert robot.get_position() == "Robot Location: (0, 0, S)"

def test_move_within_bounds(robot):
    """Test moving the robot within the grid boundaries."""
    robot.execute_commands("MMMM")
    assert robot.get_position() == "Robot Location: (4, 0, S)"

def test_turn_and_move(robot):
    """Test turning the robot and moving."""
    robot.execute_commands("MMME")
    assert robot.get_position() == "Robot Location: (3, 0, E)"
    
    robot.execute_commands("MMM")
    assert robot.get_position() == "Robot Location: (3, 3, E)"

def test_invalid_command(robot):
    """Test invalid commands and ensure they are handled."""
    user_command = "MSXMMEMM"
    valid_command, invalid_commands = robot.validate_user_command(user_command)
    assert not valid_command
    assert invalid_commands == {'X'}

def test_process_user_command(robot):
    """Test processing of user command to remove spaces and convert to uppercase."""
    processed_command = robot.process_user_command("  mm  e  s   ")
    assert processed_command == "MMES"

def test_edge_move_north_out_of_bounds(robot):
    """Test moving north out of grid bounds."""
    robot.execute_commands("NN")
    assert robot.get_position() == "Robot Location: (0, 0, N)"

def test_edge_move_east_out_of_bounds(robot):
    """Test moving east out of grid bounds."""
    robot.execute_commands("EEEEMM")
    assert robot.get_position() == "Robot Location: (0, 2, E)"

def test_edge_move_south_out_of_bounds(robot):
    """Test moving south out of grid bounds."""
    robot.execute_commands("MMMMM")
    assert robot.get_position() == "Robot Location: (4, 0, S)"

def test_edge_move_west_out_of_bounds(robot):
    """Test moving west out of grid bounds."""
    robot.execute_commands("EMMMMM")
    robot.execute_commands("WWW")
    assert robot.get_position() == "Robot Location: (0, 3, W)"

def test_turn_without_moving(robot):
    """Test turning without moving."""
    robot.execute_commands("N")
    assert robot.get_position() == "Robot Location: (0, 0, N)"

def test_complex_command(robot):
    """Test a complex sequence of commands."""
    robot.execute_commands("MSMMEMM")
    assert robot.get_position() == "Robot Location: (3, 2, E)"

def test_invalid_values_handling(robot):
    """Test that invalid characters in the command are properly handled."""
    assert robot.validate_user_command("MME@!MS") == (False, {"@", "!"})
    assert robot.validate_user_command("MME M S") == (True, None)

def test_uppercase_conversion_and_space_removal(robot):
    """Test that the process_user_command function correctly processes the user input."""
    assert robot.process_user_command("mM eW sN") == "MMEWSN"
    assert robot.process_user_command("  NNEE WWSS  ") == "NNEEWWSS"


