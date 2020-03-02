import os


def init_board():
    board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
    return board

def translate_index(lengtht, row, column):
    row_index = int(row) + int((lengtht-1)/2)
    column_index = int(column) + int((lengtht-1)/2)
    return row_index, column_index

def get_move(board, player, lengtht):
    while True:
        try:
            row = input("Enter a valid row!\n")
            column = input("Enter a valid column!\n")
            row_index, column_index = translate_index(lengtht, row, column)
            # print(row_index, column_index)
            if board[row_index][column_index] != ".":
                raise KeyError
            break
        except KeyError:
            os.system("clear")
            print_board(board)
            print(f"\n{player}'s turn")
            print("Error: invalid coordinates\033[K")
    return row_index, column_index


def choose_player(player_index):
    if int(player_index) % 2 == 1:
        player = "Player one"
    else:
        player = "Player two"
    return player


def mark(board, player, row, col):
    player_dict = {"Player one": "X", "Player two": "O"}
    board[row][col] = player_dict[player]



# def has_won(board, player):
#     player_dict = {"Player one": "X", "Player two": "O"}
#     my_boolean = False
#     for row in board:
#         if row == [player_dict[player], player_dict[player], player_dict[player]]:
#             my_boolean = True
#     for i in range(3):
#         if board[0][i] == player_dict[player] and board[1][i] == player_dict[player] and board[2][i] == player_dict[player]:
#             my_boolean = True
#     if board[0][0] == player_dict[player] and board[1][1] == player_dict[player] and board[2][2] == player_dict[player]:
#         my_boolean = True
#     if board[0][2] == player_dict[player] and board[1][1] == player_dict[player] and board[2][0] == player_dict[player]:
#         my_boolean = True
#     return my_boolean

def win_screen(board, player):
    os.system("clear")
    print_board(board)
    print(f"\n{player} won!")


def tie_screen(board, player):
    os.system("clear")
    print_board(board)
    print(f"\nIt's a tie!")


def is_full(board):
    for row in board:
        for i in range(3):
            if row[i] == ".":
                return False
    else:
        return True


def print_board(board, lengtht):
    print(" ", end="")
    for i in range(int(-(lengtht-1)/2), int((lengtht-1)/2 + 1)):
        print(f"{i}".rjust(4), end="")
    print()
    for j in range(lengtht):
        index = int(j + (1-lengtht)/2)
        print(f"{index}".rjust(3), end="")
        for i in range(lengtht-1):
            print(f"{board[j][i]}".center(3), end="|")
        print(f"{board[j][lengtht-1]}".center(3), end="")
        print()

def is_new_board(board, lengtht):
    new_board = False
    for i in range(lengtht):
        if board[0][i] != ".":
            new_board = True
        if board[i][0] != ".":
            new_board = True
        if board[lengtht - 1][i] != ".":
            new_board = True
        if board[i][lengtht - 1] != ".":
            new_board = True
    print(new_board)
    return new_board

def make_new_board(board, lengtht):
    new_board = []
    empty_row = list("." * (lengtht+2))
    new_board.append(empty_row)
    for row in board:
        new_row = ["."]
        for item in row:
            new_row.append(item)
        new_row.append(".")
        new_board.append(new_row)
    new_board.append(empty_row)
    print(new_board)
    return new_board

# def print_board(board):
#     print("1".rjust(4) + "2".rjust(4) + "3".rjust(4) + "\n")
#     print("A".ljust(2) + str(board[0][0]).center(3) + "|" + str(board[0][1]).center(3) + "|" + str(board[0][2]).center(3))
#     print("  ---+---+---")
#     print("B".ljust(2) + str(board[1][0]).center(3) + "|" + str(board[1][1]).center(3) + "|" + str(board[1][2]).center(3))
#     print("  ---+---+---")
#     print("C".ljust(2) + str(board[2][0]).center(3) + "|" + str(board[2][1]).center(3) + "|" + str(board[2][2]).center(3))

def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()
    player_index = 1
    player = "Player one"
    lengtht = 3
    while True:
        os.system("clear")
        player = choose_player(player_index)
        print_board(board, lengtht)
        print(f"\n{player}'s turn")
        row, col = get_move(board, player, lengtht)
        player = choose_player(player_index)
        print(row, col)
        mark(board, player, row, col)
        # print_board(board, lengtht)
        choice = is_new_board(board, lengtht)
        if choice == True:
            print(board)
            board = make_new_board(board, lengtht)
            lengtht += 2
        print(lengtht)
        print_board(board, lengtht)
        # if has_won(board, player) == True:
        #     win_screen(board, player)
        #     # break
        if is_full(board) == True:
            tie_screen(board, player)
            # break
        player_index += 1


# def title():
#     print("""
#     .___________. __    ______        .___________.    ___       ______        .___________.  ______    _______ 
#     |           ||  |  /      |       |           |   /   \     /      |       |           | /  __  \  |   ____|
#     `---|  |----`|  | |  ,----' ______`---|  |----`  /  ^  \   |  ,----' ______`---|  |----`|  |  |  | |  |__   
#         |  |     |  | |  |     |______|   |  |      /  /_\  \  |  |     |______|   |  |     |  |  |  | |   __|  
#         |  |     |  | |  `----.           |  |     /  _____  \ |  `----.           |  |     |  `--'  | |  |____ 
#         |__|     |__|  \______|           |__|    /__/     \__\ \______|           |__|      \______/  |_______|
                                                                                                            
# """.rjust(136))

# def main_menu():
#     title()
#     print("".center(48) + "1. Human vs Human\n")
#     print("".center(48) + "2. Human vs AI\n")
#     print("".center(48) + "3. AI vs Human\n")
#     print("".center(48) + "4. AI vs AI\n")
#     print("".center(48) + "5. Quit\n")
#     mode = input()
#     if mode == "1":
#         tictactoe_game('HUMAN-HUMAN')

# main_menu()

tictactoe_game('HUMAN-HUMAN')



# if __name__ == '__main__':
#     main_menu()
