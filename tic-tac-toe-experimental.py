# import tabulate

# def print_board(board):
#     print("1".rjust(4) + "2".rjust(4) + "3".rjust(4) + "\n")
#     print("A".ljust(2) + str(board[0][0]).center(3) + "|" + str(board[0][1]).center(3) + "|" + str(board[0][2]).center(3))
#     print("  ---+---+---")
#     print("B".ljust(2) + str(board[1][0]).center(3) + "|" + str(board[1][1]).center(3) + "|" + str(board[1][2]).center(3))
#     print("  ---+---+---")
#     print("C".ljust(2) + str(board[2][0]).center(3) + "|" + str(board[2][1]).center(3) + "|" + str(board[2][2]).center(3))

# board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
# print_board(board)
# print(tabulate(board, tablefmt="grid"))

# def translate_index(lengtht, row, column):
#     start = -(lengtht-1)/2
#     end = (lengtht-1)/2
#     for i in range(-int(start), int(end + 1)):
#         print((i, (i + (lengtht-1)/2)))


# lengtht = 7
# translate_index(lengtht, None, None)

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

board = [["X", ".", "."], [".", "O", "."], ["X", "X", "X"]]
lengtht = 3
make_new_board(board, lengtht)