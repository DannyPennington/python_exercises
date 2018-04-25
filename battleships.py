from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)


def print_board(board):
    for row in board:
        print(" ".join(row))


print ("Let's play Battleships!")
print ("")
print_board(board)


def random_row(board):
    return randint(0, len(board[0]) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(5):
    print("_______________")
    print("")
    print("Turn", turn + 1)
    guess_row = int(input("Guess Row: ")) - 1
    guess_col = int(input("Guess Col: ")) - 1

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        break
    else:
        if guess_row not in range(5) or \
                guess_col not in range(5):
            print("")
            print("Oops, that's not even in the ocean.")
            print("")
        elif board[guess_row][guess_col] == "X":
            print("")
            print("You guessed that one already.")
            print("")
        else:
            print("")
            print("You missed my battleship!")
            print("")
            board[guess_row][guess_col] = "X"
        print_board(board)
if turn == 4:
    print("")
    print("Game Over")
    print("The Battleship was at:", ship_row, ",", ship_col)


