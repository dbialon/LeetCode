# https://leetcode.com/problems/island-perimeter/
# You are given a map in form of a two-dimensional integer grid
# where 1 represents land and 0 represents water.
# Grid cells are connected horizontally/vertically (not diagonally).
# The grid is completely surrounded by water, and there is exactly
# one island (i.e., one or more connected land cells).
# The island doesn't have "lakes" (water inside that isn't connected
# to the water around the island). One cell is a square with side
# length 1. The grid is rectangular, width and height don't exceed 100.
# Determine the perimeter of the island.

from typing import List

class Solution():
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        
        perimeter = 0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    perimeter += 4
                    map_x_y = ((x-1, y), (x, y-1), (x, y+1), (x+1, y))
                    for p, q in map_x_y:
                        if 0 <= p <= rows-1 and 0 <= q <= cols-1:
                            if grid[p][q] == 1:
                                perimeter -= 1

        return perimeter


grid = [[0,1,1,0],[1,1,1,0],[0,0,1,1],[0,1,1,1]]

solution = Solution()
print(solution.islandPerimeter(grid))