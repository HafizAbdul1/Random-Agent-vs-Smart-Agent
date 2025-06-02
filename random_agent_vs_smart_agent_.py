
import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt
import tracemalloc

ROWS = 6
COLUMNS = 7
PLAYER_RANDOM = '●'
PLAYER_SMART = '○'
EMPTY = ' '

def create_board():
    return np.full((ROWS, COLUMNS), EMPTY)

def print_board(board):
    print("\n  0 1 2 3 4 5 6")
    print("  -------------")
    for row in board:
        print(" |" + '|'.join(row) + '|')
    print("  -------------")

def is_valid_location(board, col):
    return board[0][col] == EMPTY

def get_next_open_row(board, col):
    for row in reversed(range(ROWS)):
        if board[row][col] == EMPTY:
            return row
    return None

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def winning_move(board, piece):
    for r in range(ROWS):
        for c in range(COLUMNS - 3):
            if all(board[r][c+i] == piece for i in range(4)):
                return True
    for r in range(ROWS - 3):
        for c in range(COLUMNS):
            if all(board[r+i][c] == piece for i in range(4)):
                return True
    for r in range(ROWS - 3):
        for c in range(COLUMNS - 3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True
    for r in range(3, ROWS):
        for c in range(COLUMNS - 3):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True
    return False

def is_draw(board):
    return all(board[0][c] != EMPTY for c in range(COLUMNS))

def random_agent_move(board):
    valid_moves = [c for c in range(COLUMNS) if is_valid_location(board, c)]
    return random.choice(valid_moves)

def smart_agent_move(board, smart_piece, opponent_piece):
    valid_moves = [c for c in range(COLUMNS) if is_valid_location(board, c)]

    for col in valid_moves:
        temp_board = board.copy()
        row = get_next_open_row(temp_board, col)
        drop_piece(temp_board, row, col, smart_piece)
        if winning_move(temp_board, smart_piece):
            return col

    for col in valid_moves:
        temp_board = board.copy()
        row = get_next_open_row(temp_board, col)
        drop_piece(temp_board, row, col, opponent_piece)
        if winning_move(temp_board, opponent_piece):
            return col

    return random.choice(valid_moves)

def simulate_game(num_games=50):
    random_wins = 0
    smart_wins = 0
    draws = 0
    total_moves = 0

    for game in range(num_games):
        board = create_board()
        turn = game % 2
        game_over = False
        moves = 0

        while not game_over:
            if turn == 0:
                col = random_agent_move(board)
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, PLAYER_RANDOM)
                    moves += 1
                    if winning_move(board, PLAYER_RANDOM):
                        random_wins += 1
                        game_over = True
                    elif is_draw(board):
                        draws += 1
                        game_over = True
                    else:
                        turn = 1
            else:
                col = smart_agent_move(board, PLAYER_SMART, PLAYER_RANDOM)
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, PLAYER_SMART)
                    moves += 1
                    if winning_move(board, PLAYER_SMART):
                        smart_wins += 1
                        game_over = True
                    elif is_draw(board):
                        draws += 1
                        game_over = True
                    else:
                        turn = 0

        total_moves += moves

    avg_moves = round(total_moves / num_games, 2)

    df = pd.DataFrame([{
    'Matchup': 'Random vs Smart',
    'Random Wins': random_wins,
    'Smart Wins': smart_wins,
    'Draws': draws,
    'Avg Game Length (s)': avg_moves
}])

    print(df)
    return df

tracemalloc.start()

results_df = simulate_game(50)


current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024:.2f} KB")
print(f"Peak memory usage: {peak / 1024:.2f} KB")

tracemalloc.stop()

results_df.set_index('Matchup')[['Random Wins', 'Smart Wins', 'Draws']].plot(
    kind='bar',
    figsize=(8,5),
    title='Win/Draw Counts: Random vs Smart Agent',
    color=['gray', 'green', 'blue'],
    rot=0
)
plt.ylabel("Counts")
plt.grid(True)
plt.tight_layout()
plt.show()
