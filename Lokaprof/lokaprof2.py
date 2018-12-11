# Constants to be used in the implementation
DIM = 5
POSITION = 'o'
EMPTY = 'x'
LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'
QUIT = 'q'

def get_move():
    ''' Returns a move corresponding to the user input direction '''
    move = input('Move: ')
    
    if move not in [LEFT, RIGHT, UP, DOWN]:
        return QUIT
    else:
        return move

def initialize_grid():
    ''' Returns an initialized grid for the given dimension '''
    grid = []

    for i in range(DIM):
        sublist = []
        for j in range(DIM):
            sublist.append(EMPTY)
        grid.append(sublist)

    grid[0][0] = POSITION  # Current position
    
    return grid

def board(grid):
    for i in grid:
        for x in i:
            print('{:<2}'.format(x), end='')
        print('')
    
def update_grid(grid, move):
    pass

# Main program starts here
# In your implementation, you have to use the functions and the constants given above
def main():
    move = ''
    grid = initialize_grid()
    print(board(grid))
    print(grid)
    while move != QUIT:
        move = get_move()
        if move == QUIT:
            pass
        elif move == RIGHT:
            grid[0][1] = POSITION
            grid[0][0] = EMPTY
            print(board(grid))

main()