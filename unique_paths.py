# https://leetcode.com/problems/unique-paths/
# A robot is located at the top-left corner of a m x n grid
# (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid
# (marked 'Finish' in the diagram below).
# How many possible unique paths are there?


class Solution:
    def __init__(self):
        self.grid = {(1, 1): 1}
        

    def uniquePaths1(self, m: int, n: int) -> int:
        for i in range(n+1):
            for j in range(m+1):
                if (i, j) not in self.grid:
                    if i == 0 or j == 0:
                        self.grid[(i, j)] = 0
                    else:
                        self.grid[(i, j)] = self.grid[(i-1, j)] + self.grid[(i, j-1)]            

        return self.grid[(n, m)]

    
    def uniquePaths2(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if i == 1 and j == 1:
                    grid[i][j] = 1
                else:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]            

        return grid[n][m]


solution = Solution()
print(solution.uniquePaths1(3, 7))
print(solution.uniquePaths2(3, 7))
