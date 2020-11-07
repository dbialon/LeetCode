# https://leetcode.com/problems/available-captures-for-rook/
# On an 8 x 8 chessboard, there is one white rook.  There also may be
# empty squares, white bishops, and black pawns.
# These are given as characters 'R', '.', 'B', and 'p' respectively.
# Uppercase characters represent white pieces, and lowercase characters
# represent black pieces.
# The rook moves as in the rules of Chess: it chooses one of four cardinal
# directions (north, east, west, and south), then moves in that direction
# until it chooses to stop, reaches the edge of the board, or captures
# an opposite colored pawn by moving to the same square it occupies.
# Also, rooks cannot move into the same square as other friendly bishops.
# Return the number of pawns the rook can capture in one move.

from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # find the rook
        for i in range(len(board)):
            if "R" in board[i]:
                # rook's coords
                rook = (i, board[i].index("R"))
                # row containing the rook
                row = board[i]
                break
        
        # column containing the rook
        column = [column[rook[1]] for column in board]
        
        ans = 0
        
        # row going east
        for i in range(rook[1]+1, 8):
            if row[i] == "p":
                ans += 1
                break
            if row[i] == "B":
                break
        
        # row going west
        for i in range(rook[1]-1, -1, -1):
            if row[i] == "p":
                ans += 1
                break
            if row[i] == "B":
                break
        
        # column going south
        for i in range(rook[0]+1, 8):
            if column[i] == "p":
                ans += 1
                break
            if column[i] == "B":
                break
        
        # column going north
        for i in range(rook[0]-1, -1, -1):
            if column[i] == "p":
                ans += 1
                break
            if column[i] == "B":
                break
        
        return ans


board = [[".",".",".",".",".",".",".","."],
         [".",".",".","p",".",".",".","."],
         [".",".",".","p",".",".",".","."],
         ["p","p",".","R","B","p","B","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".","B",".",".",".","."],
         [".",".",".","p",".",".",".","."],
         [".",".",".",".",".",".",".","."]]

solution = Solution()
print(solution.numRookCaptures(board))
