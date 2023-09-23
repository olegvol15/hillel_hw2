import random

def create_empty_board():
    board = [[' ' for _ in range(10)] for _ in range(10)]
    return board

def print_board(player_board, computer_board):
    print("\nPlayer's Board                 Computer's Board")
    print("   A B C D E F G H I J          A B C D E F G H I J")
    for i in range(10):
        print(i, end="  ")
        for j in range(10):
            print(player_board[i][j], end=" ")
        print("      ", end="")
        for j in range(10):
            if computer_board[i][j] == 'X':
                print(' ', end=" ")
            else:
                print(computer_board[i][j], end=" ")
        print()

def manual_placement(board):
    ships = {'four-deck': 1, 'three-deck': 2, 'two-deck': 3, 'one-deck': 4}
    for ship_type, count in ships.items():
        for _ in range(count):
            print_board(board, board)
            print(f"Place {ship_type} ship ({count - _} left)")
            while True:
                try:
                    coords = input("Enter coordinates (e.g., A0) and orientation (horizontal - H, vertical - V): ").strip().upper()
                    if len(coords) != 3:
                        raise ValueError
                    x, y, orientation = coords[0], int(coords[1]), coords[2]
                    if x not in 'ABCDEFGHIJ' or y not in range(10) or orientation not in 'HV':
                        raise ValueError
                    if orientation == 'H':
                        if x > 'J' or y + len(ship_type) > 10:
                            raise ValueError
                    else:
                        if y > 9 or ord(x) - ord('A') + 1 > 10 - len(ship_type):
                            raise ValueError
                    break
                except ValueError:
                    print("Invalid coordinates. Please try again.")
            if orientation == 'H':
                for i in range(y, y + len(ship_type)):
                    board[x][i] = 'X'
            else:
                for i in range(ord(x) - ord('A'), ord(x) - ord('A') + len(ship_type)):
                    board[i][y] = 'X'
    return board

def auto_placement(board):
    ships = {'four-deck': 1, 'three-deck': 2, 'two-deck': 3, 'one-deck': 4}
    for ship_type, count in ships.items():
        for _ in range(count):
            while True:
                x, y, orientation = random.randint(0, 9), random.randint(0, 9), random.choice(['H', 'V'])
                if orientation == 'H':
                    if x > 9 or y + len(ship_type) > 10:
                        continue
                else:
                    if y > 9 or x + len(ship_type) > 10:
                        continue
                valid_placement = True
                if orientation == 'H':
                    for i in range(y, y + len(ship_type)):
                        if board[x][i] != ' ':
                            valid_placement = False
                            break
                else:
                    for i in range(x, x + len(ship_type)):
                        if board[i][y] != ' ':
                            valid_placement = False
                            break
                if valid_placement:
                    if orientation == 'H':
                        for i in range(y, y + len(ship_type)):
                            board[x][i] = 'X'
                    else:
                        for i in range(x, x + len(ship_type)):
                            board[i][y] = 'X'
                    break
    return board

def game_over(board):
    return all(all(cell != 'X' for cell in row) for row in board)

def make_move(player_board, computer_board, x, y):
    if computer_board[x][y] == 'X':
        computer_board[x][y] = 'H'
        player_board[x][y] = 'H'
        return True
    elif computer_board[x][y] == ' ':
        computer_board[x][y] = '*'
        player_board[x][y] = '*'
        return False
    return False

def computer_move(player_board):
    while True:
        x, y = random.randint(0, 9), random.randint(0, 9)
        if player_board[x][y] == ' ':
            return x, y

def main():
    print("Welcome to the Battleship game!")

    player_board = create_empty_board()
    computer_board = create_empty_board()

    print("Manual (M) or automatic (A) ship placement?")
    placement_type = input().strip().upper()

    if placement_type == 'M':
        player_board = manual_placement(player_board)
        computer_board = auto_placement(computer_board)
    elif placement_type == 'A':
        player_board = auto_placement(player_board)
        computer_board = auto_placement(computer_board)

    player_turn = True

    while True:
        print_board(player_board, computer_board)
        print("\nPlayer's turn" if player_turn else "\nComputer's turn")

        if player_turn:
            while True:
                try:
                    coords = input("Enter coordinates (e.g., A0): ").strip().upper()
                    if len(coords) != 2:
                        raise ValueError
                    x, y = coords[0], int(coords[1])
                    if x not in 'ABCDEFGHIJ' or y not in range(10):
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid coordinates. Please try again.")
            x = ord(x) - ord('A')
            if make_move(player_board, computer_board, x, y):
                print("Player hit!")
            else:
                print("Player missed.")
        else:
            x, y = computer_move(player_board)
            if make_move(player_board, computer_board, x, y):
                print("Computer hit!")
            else:
                print("Computer missed.")

        if game_over(computer_board):
            print_board(player_board, computer_board)
            print("Player wins!")
            break
        elif game_over(player_board):
            print_board(player_board, computer_board)
            print("Computer wins!")
            break

        player_turn = not player_turn

if __name__ == "__main__":
    main()


