"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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
    x_count = 0
    o_count = 0
    for i in board:
        for j in i:
            if j == X:
                x_count += 1
            if j == O:
                o_count += 1

    if o_count == x_count: 
        return X
    else:
        return O
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_set = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action_set.add((i, j))
    
    return action_set

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    play = player(board)
    board_copy = deepcopy(board)
    board_copy[action[0]][action[1]] = play
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if winner_helper(board, X) != None:
        return X
    if winner_helper(board, O) != None:
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner_helper(board, X) != None:
        return 1
    if winner_helper(board, O) != None:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    play = player(board)
    actioner = actions(board)
    save = 0

    if play == X:
        for action in actioner:
            v = minValues(result(board, action))
            if v == 1:
                return action
            elif v == 0:
                save = action
    else:
        for action in actioner:
            v = maxValues(result(board, action))
            if v == -1:
                return action
            elif v == 0:
                save = action

    if save == 0:
        return actioner[0]
    
    return save

def winner_helper (board, player):

    for i in range(3):
        count = 0
        for t in range(3):
            if board[i][t] == player:
                count += 1
        if count == 3:
            return player     

    for j in range(3):
        count = 0
        for k in range(3):
            if board[k][j] == player:
                count += 1
        if count == 3:
            return player
    
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return player
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return player
    
    return None

def maxValues (board):

    v = float("-inf")

    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = max(v, minValues(result(board, action)))
    
    return v

def minValues (board):

    v = float("inf")

    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = min(v, maxValues(result(board, action)))
    
    return v