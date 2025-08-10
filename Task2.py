import math

# Initialize board
board = [' ' for _ in range(9)]

# Print board
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Check if current player wins
def is_winner(board, player):
    win_states = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # cols
        [0,4,8], [2,4,6]            # diagonals
    ]
    return any(all(board[i] == player for i in line) for line in win_states)

# Check draw
def is_draw(board):
    return ' ' not in board

# Get available moves
def get_available_moves(board):
    return [i for i, val in enumerate(board) if val == ' ']

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if is_winner(board, 'O'):
        return 1
    elif is_winner(board, 'X'):
        return -1
    elif is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(board):
            board[move] = 'O'
            score = minimax(board, depth + 1, False)
            board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(board):
            board[move] = 'X'
            score = minimax(board, depth + 1, True)
            board[move] = ' '
            best_score = min(score, best_score)
        return best_score

# AI move
def best_move():
    best_score = -math.inf
    move = None
    for i in get_available_moves(board):
        board[i] = 'O'
        score = minimax(board, 0, False)
        board[i] = ' '
        if score > best_score:
            best_score = score
            move = i
    board[move] = 'O'

# Main game loop
def play():
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, AI is O. Enter position (1-9):")
    print_board()

    while True:
        # Human turn
        move = int(input("Your move (1-9): ")) - 1
        if board[move] != ' ':
            print("Invalid move. Try again.")
            continue
        board[move] = 'X'

        print_board()
        if is_winner(board, 'X'):
            print("🎉 You win!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        # AI turn
        print("AI is thinking...")
        best_move()
        print_board()
        if is_winner(board, 'O'):
            print("💻 AI wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

play()
