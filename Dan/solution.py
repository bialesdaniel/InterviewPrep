import random

RIGHT = 'r'
DOWN = 'd'

class Grid:
    """
    I created a class so I could reference the grid without using global variables
    """
    def __init__(self,m,n):
        """
        creates a playing board for the robot
        """
        self.columns = m
        self.rows = n
        self.board = makeBoard(m,n)

    def find_good_paths(self):
        """
        Returns an array of all the valid paths through the board
        """
        return self.robot_step((0,0),[])

    def robot_step(self, location, current_path, direction=None):
        """
        Robot tries to move in the direction specifid. If the robot can move in
        that direction it adds the direction to the path(which is the current
        steps that it has taken up to the current location). If the new space is
        the bottom right corner then it returns the path since it is a complete
        valid path. If it is not the finish we check the valid paths if the
        robot moves right or down from this location.

        If the robot cannot take the step then this returns None.
        """
        new_location = self.take_step(location, direction)
        if new_location:
            if new_location != location:
                current_path.append(direction)
            if self.is_finish(new_location):
                return [current_path]
            right = self.robot_step(new_location,list(current_path),RIGHT)
            down = self.robot_step(new_location,list(current_path),DOWN)
            if right and down:
                return right + down
            elif right:
                return right
            elif down:
                return down
            else:
                return None
        else:
            return None

    def take_step(self, location, direction):
        """
        Based on the location passed in and the direction this returns the new
        location. If the new location is not valid it returns None

        If no direction is specified then it returns the current location (this)
        is for the first space)
        """
        if direction == RIGHT:
            step_location = (location[0]+1,location[1])
        elif direction == DOWN:
            step_location = (location[0], location[1]+1)
        else:
            return location

        if step_location[1] < self.rows and step_location[0] < self.columns:
            return step_location if self.is_space_open(step_location) else None

    def is_space_open(self, location):
        """
        True if the location is not blocked, False otherwise.
        """
        return self.board[location[1]][location[0]] == 0

    def is_finish(self,location):
        """
        True if the location is the bottom right most space
        """
        return location[0] == self.columns - 1 and location[1] == self.rows - 1

    def print_board(self):
        """
        print out a visual representation of the board in the terminal
        """
        print('Board:')
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.board]))


def makeBoard(m,n):
    """
    Randomly create a playing board. Spaces have a value of 0 or 1. 1 indicates
    that the space is blocked and the robot cannot step there. The top right
    and bottom left spaces are always open.
    """
    if m < 2 or n < 2:
        raise ValueError('Grid must be at least 2x2')
    grid = []
    for y in range(n):
        row = []
        for x in range(m):
            value = 1 if random.randint(0,4) % 4 == 0 else 0
            if x==0 and y==0:
                value = 0
            if x==(m-1) and y==(n-1):
                value = 0
            row.append(value)
        grid.append(row)
    return grid

if __name__ == '__main__':
    grid = Grid(10,10)
    grid.print_board()
    good_paths  = grid.find_good_paths()
    print('Paths: {}'.format(str(good_paths)))
    answer = len(good_paths) if good_paths else 0
    print('Answer: {}'.format(answer))
