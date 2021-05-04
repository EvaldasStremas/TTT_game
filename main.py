import copy
import os

NUM_ROWS = 3
NUM_COLS = 3
EMPTY_SYMBOL = " "

def get_empty_grid(num_cols, num_rows, empty_symbol):
    grid = []

    for x in range(num_rows):
        row = []
        for _ in range(num_cols):
            row.append(empty_symbol)
        grid.append(row)
    return grid

def print_grid(grid):
    for i in range(NUM_ROWS):
        print(grid[i])

# ------------------------------------MAIN-----------------------------------------

def main():
    finish_game = 0
    grid = get_empty_grid(NUM_COLS, NUM_ROWS, EMPTY_SYMBOL)

    while finish_game < 1:

        os.system('cls' if os.name == 'nt' else 'clear')

        print_grid(grid)
        print()

        print('First player: Where add "X" symbol?')
        x_value_x_axis = int(input('In X axis (0..2): '))
        x_value_y_axis = int(input('In Y axis (0..2): '))

        grid[x_value_y_axis][x_value_x_axis] = 'X'

        os.system('cls' if os.name == 'nt' else 'clear')

        print_grid(grid)
        print()

        print('Second player: Where add "O" symbol?')
        o_value_x_axis = int(input('In X axis (0..2): '))
        o_value_y_axis = int(input('In Y axis (0..2): '))

        grid[o_value_y_axis][o_value_x_axis] = 'O'

        os.system('cls' if os.name == 'nt' else 'clear')

        print_grid(grid)

        points = [
        [[0, 0], [0, 1], [0, 2]], # 1 horizontal line
        [[1, 0], [1, 1], [1, 2]], # 2 horizontal line
        [[2, 0], [2, 1], [2, 2]], # 3 horizontal line
        [[0, 0], [1, 0], [2, 0]], # 1 vertical line
        [[0, 1], [1, 1], [2, 1]], # 2 vertical line
        [[0, 2], [1, 2], [2, 2]],  # 3 vertical line
        [[2, 2], [1, 1], [0, 0]], # \ cross line
        [[2, 0], [1, 1], [0, 2]]  # / cross line
        ]

        lines_counter = []
        lines_counter_list = []
        x_list = []

        for z in range(len(points)):
            for c in range(len(points[z])):
                lines_counter.append(grid[points[z][c][0]][points[z][c][1]])

            lines_counter_list.append(lines_counter)
            x_counter = lines_counter.count("X")
            x_list.append(x_counter)
            lines_counter = []
        print(x_list)

        for i in range(len(x_list)):
            if x_list[i] == 3:
                print('Winner is X palyer')
                finish_game = 1

        print()
        input("Press ENTER")

if __name__ == '__main__':
    main()