# https://leetcode.com/problems/remove-element/
# with a given list and a value this function is to
# find that value in the list and either replace it or
# move it within the list
# no memory allocation is allowed for a new list
# the function is also to return the length of the list
# so that slice will contain viable items only
# what is beyond that point is not important


def remove_element(alist, value):
	if len(alist) == 0:
		return 0

	j = 0
	for i in range(len(alist)):
		if alist[i] != value:
			alist[j] = alist[i]
			j += 1

	return j


my_list = [1, 1, 2, 3, 4, 5, 6, 6, 7, 8, 8]

print(my_list[:remove_element(my_list, 6)])

# time complexity of O(N) as we traverse the list just once

# space compexity of O(1) as an extra space has been added for a variable
