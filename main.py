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


def enter_player_input(player_indication, grid):
    # Checking X or O player enter input is valid integer
    os.system('cls' if os.name == 'nt' else 'clear')  # 1

    print_grid(grid)

    # print('PLAYER ', player_indication)

    while True:
        # This while loop stands for checking is x and y axis points is already not used in grid
        try:
            while True:
                # This while loop stands for checking valid x axis integer
                try:
                    print('PLAYER ', player_indication)
                    x_axis = input('Enter integer in X axis (From 0 to 2): ')
                    x_axis = int(x_axis)
                    break
                except ValueError:
                    print("No valid integer! Please try again ...")
                # except IndexError:
                #     print("Value should be from 0 to 2! Please try again ...")

            while True:
                # This while loop stands for checking valid y axis integer
                try:
                    print('PLAYER ', player_indication)
                    y_axis = input('Enter integer in Y axis (From 0 to 2): ')
                    y_axis = int(y_axis)
                    break
                except ValueError:
                    print("No valid integer! Please try again ...")
                # except IndexError:
                #     print("Value should be from 0 to 2! Please try again ...")

            if grid[y_axis][x_axis] != "X" and grid[y_axis][x_axis] != "O":
                grid[y_axis][x_axis] = player_indication
                break
            else:
                print('Window is already used in grid! Please try again ...')
                input("Press ENTER")
                os.system('cls' if os.name == 'nt' else 'clear')
                print_grid(grid)

        except ValueError:
            print()

    return grid


def check_winner(player_indication, grid):
    # Check is player X or O is winner
    points = [
        [[0, 0], [0, 1], [0, 2]],  # 1 horizontal line
        [[1, 0], [1, 1], [1, 2]],  # 2 horizontal line
        [[2, 0], [2, 1], [2, 2]],  # 3 horizontal line
        [[0, 0], [1, 0], [2, 0]],  # 1 vertical line
        [[0, 1], [1, 1], [2, 1]],  # 2 vertical line
        [[0, 2], [1, 2], [2, 2]],  # 3 vertical line
        [[2, 2], [1, 1], [0, 0]],  # \ cross line
        [[2, 0], [1, 1], [0, 2]]  # / cross line
    ]

    lines_counter = []
    result_list = []

    all_players_result = get_all_players_result(player_indication, grid)

    for z in range(len(points)):
        for c in range(len(points[z])):
            lines_counter.append(grid[points[z][c][0]][points[z][c][1]])

        result_counter = lines_counter.count(player_indication)
        result_list.append(result_counter)
        lines_counter = []
    # print(result_list)
    # print(all_players_result)
    input("Press ENTER")

    os.system('cls' if os.name == 'nt' else 'clear')  # 1

    if 3 in result_list:
        print('Winner is ', player_indication, ' palyer')
        game_over = True
        return game_over

    if all_players_result == 9:
        print('Grid is full. Game ended.')
        game_over = True
        return game_over

    print()


def get_all_players_result(player_indication, grid):
    all_grid_elements_list = []

    for nums in range(NUM_ROWS):
        for cols in range(NUM_COLS):
            all_grid_elements_list.append(grid[nums][cols])
    x_player_results = all_grid_elements_list.count('X')
    o_player_results = all_grid_elements_list.count('O')
    all_grid_elements_values = x_player_results + o_player_results

    return all_grid_elements_values


# ------------------------------------MAIN-----------------------------------------

def main():
    game_over = False
    grid = get_empty_grid(NUM_COLS, NUM_ROWS, EMPTY_SYMBOL)

    while not game_over:

        grid = enter_player_input('X', grid)
        game_over = check_winner('X', grid)

        if game_over == True:
            break

        grid = enter_player_input('O', grid)
        game_over = check_winner('O', grid)

        print_grid(grid)

        print()


if __name__ == '__main__':
    main()