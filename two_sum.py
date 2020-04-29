# function that returns indices of two items
# from a list if their sum is known


def two_sum(alist, thesum):
	# list that will contain the indices of the two items
	# we're looking for
	result = list()

	# this dictionary will contain items from the input list
	# as keys and their indices as dictionary values
	table = dict()

	for item in alist:
		# value will be in the table only if the current item
		# is a match to 'thesum - item' item
		value = thesum - item

		if value not in table:
			# not a match, we need to add it for future comparisons
			table[item] = alist.index(item)
		else:
			result.append(table[value])
			result.append(alist.index(item))
			break

	return result

my_list = [1, 2, 5, 6, 8, 14, 19]

print(two_sum(my_list, 33))

# the purpose of using a dictionary (hashtable) is to
# reduce time complexity of this method
# we iterate over the list just once so O(N)
# space complecity: O(N) for the dictionary
# and O(1) for variables so O(N)