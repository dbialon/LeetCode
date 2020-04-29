# https://leetcode.com/problems/degree-of-an-array/
# given a non-empty array of non-negative integers nums,
# the degree of this array is defined as the maximum frequency
# of any one of its elements.
# find the smallest possible length of a (contiguous)
# subarray of nums, that has the same degree as nums.

from collections import Counter

def findShortestSubArray(nums) -> int:
	counter = dict()

	for i in range(len(nums)):
		if nums[i] not in counter:
			counter[nums[i]] = [1]
			counter[nums[i]].extend((i, i))
		else:
			counter[nums[i]][0] += 1
			counter[nums[i]][2] = i

	# print(counter)

	min_sub_len = len(nums)
	max_degree = 0
	for key in counter:
		if counter[key][0] > max_degree:
			max_degree = counter[key][0]
			min_sub_len = counter[key][2] - counter[key][1] + 1
		elif counter[key][0] == max_degree:
			if counter[key][2] - counter[key][1] + 1 < min_sub_len:
				min_sub_len = counter[key][2] - counter[key][1] + 1

	return min_sub_len

	#first = nums.index(1)
	#last = first
	#while True:
		# last += 1
		# try:
		# 	nums.index(1, last)
		# except ValueError:
		# 	print("error")
		# 	last -= 1
		# 	print(last)
		# 	print(nums)
		# 	print("Indices:", first, last)
		# 	print("Answer:", last - first)
		# 	break

# my_list = [1]
my_list = [1,2,2,3,1]
# my_list = [1, 0, 5, 4, 4, 2, 4, 7, 8, 8, 9, 5, 1, 1]

print(findShortestSubArray(my_list))