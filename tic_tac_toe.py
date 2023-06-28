"""Create the grid for the game"""
grid = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]

"""Entry point into the program"""


def main():
    print("Welcom to the Tic Tac Toe Game")
    display_grid()
    start_game()


def start_game():
    game_over = False
    while not game_over:
        game_over = take_turn()
    print()
    print("Game Over!")


"""This function is responsible for determining a winner"""


def take_turn():
    turn = 1
    while True:
        if not turn % 2 == 0:
            mark = "X"
        else:
            mark = "O"
        print(f"{mark}'s turn")

        row = int(input("Pick a row (1, 2, 3):"))
        if row < 1 or row > 3:
            print("Invalid row number. Try again.")
            continue

        column = int(input("Please enter a column (1, 2, 3):"))
        if column < 1 or column > 3:
            print("Invalid column number. Try again.")
            continue

        if not grid[row-1][column-1] == " ":
            print("This position is aleady occupied. Try again.")
            continue

        grid[row-1][column-1] = mark
        display_grid()

        winner = check_for_winner()
        if winner == "X" or winner == "O":
            print(f"{winner} wins this game!")
            game_over = True
            return game_over

        if turn == 9:
            print("It is a tie!")
            game_over = True
            return game_over

        turn += 1


"""The fuction responsible for drawing the game grid"""


def display_grid():
    print()
    print("+---+---+---+")
    for row in grid:
        print("|", end="")
        for column in row:
            print(f" {column} |", end="")
        print()
        print("+---+---+---+")
    print()


"""Compare combinations to determine winner"""


def check_for_winner():
    # check the rows
    for x in range(3):
        if grid[x][0] == grid[x][1] == grid[x][2]:
            return grid[x][0]

    # check the columns
    for y in range(3):
        if grid[0][y] == grid[1][y] == grid[2][y]:
            return grid[0][y]

    # check for diagonal 1
    if grid[0][0] == grid[1][1] == grid[2][2]:
        return grid[0][0]

    # check for diagonal 2
    if grid[0][2] == grid[1][1] == grid[2][0]:
        return grid[0][2]

    # no winner yet
    return " "


"""Start with the main() function"""
if __name__ == "__main__":
    main()
