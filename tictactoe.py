"""
Tic-Tac-Toe: A Game
Author: Richard O
"""

# Define a main function 
def main():
    player = switch_player("")
    board = draw_board()
    while not (a_winner(board) or a_draw(board)):
        display_board(board)
        make_move(player, board)
        player = switch_player(player)
    display_board(board)
    print(f"Congratulations! We have a winner!!!")

# Draw the board
def draw_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

# Display board
def display_board(board):
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+")
    print(f"{board[6]}|{board[7]}|{board[8]}")

# Define when there is a draw
def a_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True

# Define when there is a winner
def a_winner(board):
    return (board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8]\
    or board[0] == board[4] == board[8] or board[2] == board[4] == board[6] or board[0] == board[3] == board[6]\
    or board[2] == board[5] == board[8])

# Player needs to make a move
def make_move(player, board):
    square = int(input(f"{player}'s turn to play: "))
    board[square - 1]= player

# Choose current player
def switch_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"
    elif current == "x" or current == "o":
        return current


# Call the main function
if __name__ == "__main__":
    main()