"""
Tic Tac Toe Player
"""


import math
import copy
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    if board == initial_state():
        return X
    
    count_x = 0
    count_o = 0
    for row in board:
        count_x += row.count(X)
        count_o += row.count(O)
    
    if count_x == count_o:
        return X
    else:
        return O


def actions(board):
    posible_actions = set()

    for row_index, row in enumerate(board):
        for cell_index, cell in enumerate(row):
            if(cell == EMPTY):
                posible_actions.add((row_index, cell_index))

    return posible_actions


def result(board, action):
    
    if board[action[0]][action[1]] != EMPTY:
        raise Exception('Cell is not empty')
    
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)

    return new_board


def winner(board):
    board_validation = board.copy() + [[board[0][0], board[1][0], board[2][0]]] + [[board[0][1], board[1][1], board[2][1]]] + [[board[0][2], board[1][2], board[2][2]]] + [[board[0][0], board[1][1], board[2][2]]] + [[board[0][2], board[1][1], board[2][0]]]

    for validation_field in board_validation:
        if validation_field.count(X) == 3:
            return X
        if validation_field.count(O) == 3:
            return O

    return None


def terminal(board):
    if winner(board) != EMPTY:
        return True
    
    empty_count = 0
    for row in board:
        empty_count += row.count(EMPTY)

    return empty_count == 0


def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def boards_validation(board):
    if terminal(board):
        return utility(board), ()
    
    list_actions = list(actions(board))

    if player(board) == X:
        best_score = -math.inf
        best_action = ()
        for action in list_actions:
            new_board = result(board,action)
            validation = boards_validation(new_board)
            if max(best_score, validation[0]) == validation[0]:
                best_score = validation[0]
                best_action = action
        
        return best_score, best_action

    else:
        best_score = math.inf
        for action in list_actions:
            new_board = result(board,action)
            validation = boards_validation(new_board)
            if min(best_score, validation[0]) == validation[0]:
                best_score = validation[0]
                best_action = action
        
        return best_score, best_action


def minimax(board):

    if board == initial_state():
        list_actions = list(actions(board))
        first_move = list_actions[random.randint(0, len(list_actions) - 1)]
        return first_move

    result = boards_validation(board)
    return result[1]
