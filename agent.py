# Andrew Edwards -- almostimplemented.com
# =======================================
# A checkers agent class.
#
# Last updated: July 21, 2014


class CheckersAgent:
    def __init__(self, move_function, return_moves):
        self.move_function = move_function
        self.return_moves = return_moves
    def return_moves(self, board):
        return self.return_moves(board)
    
    def make_move(self, board):
        return self.move_function(board)

    def return_moves(self, board):
        return self.return_moves(board)
