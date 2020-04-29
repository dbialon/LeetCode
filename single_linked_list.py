class Node(object):
	def __init__(self, data=None, link=None):
		self.data = data
		self.link = link

	def __repr__(self):
		return repr(self.data)

class Sllist:
	def __init__(self):
		self.head = None

	def __repr__(self):
		nodes = list()
		curr = self.head
		while curr:
			nodes.append(repr(curr))
			curr = curr.link

		return "[" + ", ".join(nodes) + "]"

	def prepend(self, data):
		self.head = Node(data=data, link=self.head)

root = Sllist()

root.prepend(2)

print("root", root)