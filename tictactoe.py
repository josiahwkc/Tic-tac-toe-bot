"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None



def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_moves = 0
    o_moves = 0
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_moves += 1
            elif board[i][j] == O:
                o_moves += 1
    
    if x_moves == o_moves:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions_set.add((i,j))
                
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j = action
    if board[i][j] != EMPTY:
        raise ValueError(f"Invalid action: position ({i}, {j}) is already filled.")
    
    new_board = copy.deepcopy(board)    
    new_board[i][j] = player(new_board)
    
    return new_board
     

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # 3 in a horizontal row
    for row in range(3):
        if board[row][0] != None and board[row][0] == board[row][1] == board [row][2]:
            return board[row][0]
        
    # 3 in a vertical line
    for col in range(3):
        if board[0][col] != None and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]
        
    # 3 in a diagonal
    if (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]):
        return board[1][1]
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if winner(board) is None:
        for i in range(3):
            for j in range(3):
                if board[i][j] == None:
                    return False
    return True
    
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    if player(board) == X:
        value, action = max_alpha_beta_pruning(board, float('-inf'), float('inf'))
    elif player(board) == O:
        value, action = min_alpha_beta_pruning(board, float('-inf'), float('inf'))
        
    return action
    
def max_value(board):
    """
    Returns the highest value of min_value()
    """
    value = float('-inf')
    optimal_action = None
        
    if terminal(board):
        return utility(board), None
    
    for action in actions(board):
        min_val, _ = min_value(result(board, action))
        if min_val > value:
            value = min_val
            optimal_action = action
        
    return value, optimal_action

def min_value(board):
    """
    Returns the lowest value of max_value()
    """
    value = float('inf')
    optimal_action = None
    
    if terminal(board):
        return utility(board), None
    
    for action in actions(board):
        max_val, _ = max_value(result(board, action))
        if max_val < value:
            value = max_val
            optimal_action = action
        
    return value, optimal_action

def max_alpha_beta_pruning(board, alpha, beta):
    """
    Returns the highest value of min_value()
    """
    optimal_action = None
        
    if terminal(board):
        return utility(board), None
    
    for action in actions(board):
        min_val, _ = min_alpha_beta_pruning(result(board, action), alpha, beta)
        if min_val > alpha:
            alpha = min_val
            optimal_action = action
        if alpha >= beta:
            break
        
    return alpha, optimal_action

def min_alpha_beta_pruning(board, alpha, beta):
    """
    Returns the lowest value of max_value()
    """
    optimal_action = None
    
    if terminal(board):
        return utility(board), None
    
    for action in actions(board):
        max_val, _ = max_alpha_beta_pruning(result(board, action), alpha, beta)
        if max_val < beta:
            beta = max_val
            optimal_action = action
        if alpha >= beta:
            break
        
    return beta, optimal_action