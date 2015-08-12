"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
#import codeskulptor
#codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    
    
    if(board.check_win() != None):
        return SCORES[board.check_win()], (-1,-1)

    moves = {}
    max_score = -1

    for move_branch in board.get_empty_squares():
        current_board = board.clone()
        current_board.move(move_branch[0],move_branch[1], player)
        moves[move_branch] = mm_move(current_board, provided.switch_player(player))
        current_score = moves[move_branch][0]*SCORES[player]
        if( current_score == 1):
           return current_score*SCORES[player], move_branch #reached best case, break out
        if(current_score > max_score):
            max_score = current_score

    for move in moves:
        if(moves[move][0]*SCORES[player]== max_score):
            return moves[move][0], move
        
    return 'error', (-1, -1)

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)

