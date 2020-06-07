import random

RIGHT = 'r'
DOWN = 'd'

class Grid:
    def __init__(self,m,n):
        self.columns = m
        self.rows = n
        self.board = makeGrid(m,n)

    def find_good_paths(self):
        return self.robot_step((0,0),[])

    def robot_step(self, location, current_path, direction=None):
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
        if direction == RIGHT:
            step_location = (location[0]+1,location[1])
        elif direction == DOWN:
            step_location = (location[0], location[1]+1)
        else:
            return location

        if step_location[1] < self.rows and step_location[0] < self.columns:
            return step_location if self.is_space_open(step_location) else None

    def is_space_open(self, location):
        return self.board[location[1]][location[0]] == 0

    def is_finish(self,location):
        return location[0] == self.columns - 1 and location[1] == self.rows - 1

    def print_board(self):
        print('Board:')
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.board]))


def makeGrid(m,n):
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
