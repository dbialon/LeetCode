class Solution:
    powers_of_2 = {2**n for n in range(64)}
    def isPowerOfTwo(self, n: int) -> bool:
        if n in self.powers_of_2:
            return True
        else:
            return False


####################
### TESTING ONLY ###
####################

solution = Solution()
for number in range(17):
    print(number, solution.isPowerOfTwo(number))
