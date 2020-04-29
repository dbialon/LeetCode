# https://leetcode.com/problems/move-zeroes/
# given an array nums, write a function to move
# all 0's to the end of it while maintaining
# the relative order of the non-zero elements.

def moveZeroes(nums: [int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    l = len(nums)
    for i in range(l):
        if nums[i] == 0:
            for j in range(i, l):
                if nums[j] != 0:
                    nums[i] = nums[j]
                    nums[j] = 0
                    break
            else:
                return None

my_list = [0, 0, 0, 1, 0, 2, 3, 4, 5, 0, 6]

moveZeroes(my_list)
print(my_list)
