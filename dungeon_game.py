# https://leetcode.com/problems/dungeon-game/
# The demons had captured the princess (P) and imprisoned her in the
# bottom-right corner of a dungeon. The dungeon consists of M x N rooms
# laid out in a 2D grid. Our valiant knight (K) was initially positioned
# in the top-left room and must fight his way through the dungeon to
# rescue the princess.
# The knight has an initial health point represented by a positive
# integer. If at any point his health point drops to 0 or below,
# he dies immediately.
# Some of the rooms are guarded by demons, so the knight loses health
# (negative integers) upon entering these rooms; other rooms are either
# empty (0's) or contain magic orbs that increase the knight's health
# (positive integers).
# In order to reach the princess as quickly as possible, the knight
# decides to move only rightward or downward in each step.
# Write a function to determine the knight's minimum initial health
# so that he is able to rescue the princess.

from typing import List
from itertools import permutations

class Solution:
    '''
        this method fails for large dungeons as number of paths equals
        factorial(rows+columns)
    '''
    def calculateMinimumHP_1(self, dungeon: List[List[int]]) -> int:
        if len(dungeon) == 1 and len(dungeon[0]) == 1:
            if dungeon[0][0] < 0:
                return -dungeon[0][0] + 1
            else:
                return 1

        max_x = len(dungeon[0]) - 1 # columns
        max_y = len(dungeon) - 1    # rows
        steps = "R" * max_x + "D" * max_y
        paths = set()
        for perm in permutations(steps):
            paths.add(perm)
        paths = list(paths)
        
        result = None
        for path in paths:
            initial_hp = 1 if dungeon[0][0] >= 0 else -dungeon[0][0] + 1
            surplus = 0 if dungeon[0][0] < 0 else dungeon[0][0]
            x, y = 0, 0
            for step in path:
                if step == "R":
                    x += 1
                else:
                    y += 1
                if dungeon[y][x] < 0:             # use surplus or/and loose hp
                    if surplus >= -dungeon[y][x]: # cell is negative
                        surplus += dungeon[y][x]  # subtract from surplus
                    else:
                        initial_hp -= surplus + dungeon[y][x] # subtract because it's neg already
                        surplus = 0 # all surplus has been used
                else:
                    surplus += dungeon[y][x] # build up surplus
            
            if result is None or initial_hp < result:
                result = initial_hp
        
        return result

    
    def calculateMinimumHP_2(self, dungeon: List[List[int]]) -> int:
        '''
            dynamic programming method
            we create a new list of the same size as dungeon and fill it
            with zeroes; starting with the last cell ([-1][-1]) we calculate
            the minimum number of points required to enter that cell and then
            go backwards towards the entrance; if the cell has negative value
            we need to add it to the value of the previous cell; the cells on
            the edges have only one cell to take consideration into while cells
            in the middle have 2, therefore we choose the one with lower value
        '''
        max_x = len(dungeon) - 1 # rows
        max_y = len(dungeon[0]) - 1    # columns
        min_hp = [[0 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]
        
        # fill up last cell
        if dungeon[max_x][max_y] < 0:
            min_hp[max_x][max_y] = -dungeon[max_x][max_y] + 1
        else:
            min_hp[max_x][max_y] = 1

        # fill up last column
        for p in range(max_x-1,-1,-1):
            min_hp[p][max_y] = max(min_hp[p+1][max_y] - dungeon[p][max_y], 1)

        # fill up last row
        for q in range(max_y-1,-1,-1):
            min_hp[max_x][q] = max(min_hp[max_x][q+1] - dungeon[max_x][q], 1)

        # fill up the rest of the array
        for p in range(max_x-1,-1,-1):
            for q in range(max_y-1,-1,-1):
                min_hp[p][q] = max(min(min_hp[p][q+1], min_hp[p+1][q]) - dungeon[p][q], 1)

        return min_hp[0][0]


dungeon = [[-3]]
# dungeon = [[-2,-3,3],
#            [-5,-10,1],
#            [10,30,-5]]
# dungeon = [[0,-74,-47,-20,-23,-39,-48],
#            [37,-30,37,-65,-82,28,-27],
#            [-76,-33,7,42,3,49,-93],
#            [37,-41,35,-16,-96,-56,38],
#            [-52,19,-37,14,-65,-42,9],
#            [5,-26,-30,-65,11,5,16],
#            [-60,9,36,-36,41,-47,-86],
#            [-22,19,-5,-41,-8,-96,-95]]


solution = Solution()
print(solution.calculateMinimumHP_1(dungeon))
print(solution.calculateMinimumHP_2(dungeon))
