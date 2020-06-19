# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# function that removes duplicates of a sorted list
# creating a new list is not allowed
# function has to return the length of a duplicate-free list
# it doesn't matter what the list contains beyond duplicate-free part
# no new memory allocation is allowed
from typing import List

class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		# if the list is empty return 0
		if len(nums) == 0:
			return 0

		# j is a cursor which moves forward only when an item
		# different than that, under the cursor, is found
		j = 0
		for item in nums:
			if item != nums[j]:
				j += 1
				nums[j] = item

		# we return j + 1 as that's the length of the non-duplicate list
		return j + 1

nums = [1, 1, 2, 2, 2, 2, 3, 4, 5, 5, 5, 5, 6, 6, 7, 8, 8, 9, 9]

solution = Solution()
length = solution.removeDuplicates(nums)
print(nums[:length])

# time complexity O(N) as we traverse the list just once

# space complexity O(1) as we create one new variable
