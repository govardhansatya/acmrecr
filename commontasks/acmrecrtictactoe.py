#toe pics
import random as rd
def print_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
def winner(board, player):
    win = [(0, 1, 2),(3, 4, 5),(6, 7, 8),(0, 3, 6),(1, 4, 7),(2, 5, 8),(0, 4, 8),(2, 4, 6)]
    for combo in win:
        if all(board[i] == player for i in combo):
            return True
    return False
def filled(board):
    return all(cell != " " for cell in board)
def valid_move(board):
    return [i for i, cell in enumerate(board) if cell == " "]
def ari_move(board):
    valid_moves = valid_move(board)
    return rd.choice(valid_moves)
def tic_tac_toe():
    board = [" "] * 9
    players = ["X", "O"]
    current_player = 0
    human_player = "X"
    ai_player = "O"

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        if current_player == 0:
            print("Your turn")
            while True:
                try:
                    move = int(input("Enter your move (1-9): ")) - 1
                    if move < 0 or move > 8 or board[move] != " ":
                        raise ValueError
                    break
                except ValueError:
                    print("Error! select non empty cell")
        else:
            print("my turn")
            move = ari_move(board)
            print(f"i choose {move + 1}")
        board[move] = players[current_player]
        print_board(board)

        if winner(board, players[current_player]):
            if current_player == 0:
                print("You win!")
            else:
                print("I won!")
            break

        if filled(board):
            print("It's a draw!")
            break

        current_player = 1 - current_player

tic_tac_toe()