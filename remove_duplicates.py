# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# function that removes duplicates of a sorted list
# creating a new list is not allowed
# function has to return the length of a duplicate-free list
# it doesn't matter what the list contains beyond duplicate-free part
# no new memory allocation is allowed

def remove_duplicates(alist):
	# if the list is empty return 0
	if len(alist) == 0:
		return 0

	# we have 2 cursors i and j
	# i is leading and j is following
	# j moves forward only if i finds a new value not equal to j-th item
	# when it does, the j-th item gets the value of that item
	j = 0
	for i in range(1, len(alist)):
		if alist[i] != alist[j]:
			j += 1
			alist[j]= alist[i]

	# we return j + 1 as that's the length of the non-duplicate list
	return j + 1

my_list = [1, 1, 2, 2, 2, 2, 3, 4, 5, 5, 5, 5, 6, 6, 7, 8, 8, 9, 9]

# length = remove_duplicates(my_list)
# print(my_list[:length])

print(my_list[:remove_duplicates(my_list)])

# time complexity O(N) as we traverse the list just once

# space complexity O(1) as we create one new variable
