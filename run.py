from random import randint

#Board for  ship position
CACHE_BOARD = [[" "] * 8 for x in range(8)]
# Board for running points and missing targets
IMAGINE_BOARD = [[" "] * 8 for i in range(8)]

def print_board(board):
    print("  A B C D E F G H ")
    print(" +---------------+ ")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

letters_to_numbers = {

    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    
}

def create_ships(board):
    """
     5 ships creating by computer
    """
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"

def get_ship_location():
    row = input("Enter the row of the ship:\n ").upper()
    while row not in "12345678":
        print('A selection of valid row is required')
        row = input("Enter the row of the ship:\n ").upper()
    column = input("Enter the column of the ship:\n ").upper()
    while column not in "ABCDEFGH":
        print('A correct column selection is required')
        column = input("Enter the column of the ship: ").upper()
    return int(row) - 1, letters_to_numbers[column]


def count_hit_ships(board):

    """
    validation of touched ships
    """
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

if __name__ == "__main__":
    create_ships(CACHE_BOARD)
    turns = 15
    while turns > 0:
        print('Welcome to our battleships competition\nGuess a battleship location')
        print_board(IMAGINE_BOARD)
        row, column = get_ship_location()
        if IMAGINE_BOARD[row][column] == "-":
            print("You guessed that one already.")
        elif CACHE_BOARD[row][column] == "X":
            print("BRAVO")
            IMAGINE_BOARD[row][column] = "X" 
            turns -= 1  
        else:
            print("SORRY!")
            IMAGINE_BOARD[row][column] = "-"   
            turns -= 1     
        if count_hit_ships(IMAGINE_BOARD) == 5:
            print("You got them!")
            break
        print("You have " + str(turns) + " turns left")
        if turns == 0:
            print("Game Over")

