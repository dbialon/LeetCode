# https://leetcode.com/problems/prison-cells-after-n-days/

# There are 8 prison cells in a row, and each cell is either occupied
# or vacant. Each day, whether the cell is occupied or vacant changes
# according to the following rules:
# If a cell has two adjacent neighbors that are both occupied or both
# vacant, then the cell becomes occupied. Otherwise, it becomes vacant.
# (Note that because the prison is a row, the first and the last cells
# in the row can't have two adjacent neighbors.)
# We describe the current state of the prison in the following way:
# cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.
# Given the initial state of the prison, return the state of the prison
# after N days (and N such changes described above.)

from typing import List

class Solution:
    '''
        'cells' array can be considered as an 8-bit long integer since
        it consists of 0s and 1s only, therefore there are 2**8 unique
        inputs; outputs though will always have 0 as the first and
        the last bit so there are 2**6 unique outputs; that means that
        after k days the cells array will come to the same configuration;
        after testing it's been determined that it is 14 days for
        non-symmetrical arrays and 7 days for symmetrical arrays
        ([1,0,0,1,1,0,0,1] or even 1 day for [0,0,1,0,0,1,0,0])
    '''
    def __init__(self):
        self.cycles = [None for _ in range(256)]
        for n in range(256):
            binary = bin(n)[2:]
            array = ['0' for _ in range(8)]
            i = 7
            for letter in binary[::-1]:
                array[i] = letter
                i -= 1
            self.cycles[n] = int(''.join(self.initialConversion(array)), 2)


    def initialConversion(self, array: List[str]) -> List[str]:
        buffer = [array[0], None]
        for i in range(1, 7):
            buffer[1] = array[i]
            if buffer[0] == array[i+1]:
                array[i] = '1'
            else:
                array[i] = '0'
            buffer[0] = buffer[1]
        array[0], array[-1] = '0', '0'

        return array

    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        # cycle repeats every 14 days after day 1 (1, 15, ...)
        N %= 14 # we count from '0'
        if N == 0:
            N = 14

        number = int(''.join([str(i) for i in cells]), 2)
        for n in range(N):
            number = self.cycles[number]

        binary = bin(number)[2:]
        binary = (8 - len(binary)) * '0' + binary 
        cells = [int(letter) for letter in binary]

        return cells


cells = [1,0,0,1,1,0,0,1]
# cells = [1,1,1,1,1,0,1,1]
print(cells)

solution = Solution()
print(solution.prisonAfterNDays(cells, 17))
