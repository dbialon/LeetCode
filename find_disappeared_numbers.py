from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:        
        l = len(nums)

        for i in range(l):
            while nums[nums[i]-1] != nums[i]:
                tmp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = tmp

        result = []
        for i in range(l):
            if nums[i] != i+1:
                result.append(i+1)

        return result


nums = [4,3,2,3,8,2,7,1]

solution = Solution()
print(solution.findDisappearedNumbers(nums))