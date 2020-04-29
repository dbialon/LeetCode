# https://leetcode.com/problems/maximum-subarray/

def max_subarray_sum(alist):
	max_ending_here = alist[0]
	max_so_far = alist[0]

	for i in range(1, len(alist)):
		max_ending_here = max(max_ending_here + alist[i], alist[i])

		max_so_far = max(max_ending_here, max_so_far)
	return max_so_far

my_list = [-1, 2, -2, 3, 4, -1, -2, 4, -3, 2]

print(max_subarray_sum(my_list))