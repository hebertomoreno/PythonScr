'''The node class is initialized with no linked nodes, because they will be assigned as 
they are inserted into the LinkedList'''
class Node(object):
	#Node class constructor
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next_node

	def set_next(self, new_next):
		self.next_node = new_next

class LinkedList(object):
	#LinkedList class constructor
	def __init__(self, head=None):
		self.head = head

	#Inserts a new node into the list
	def insert(self, data):
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node

	#Counts the number of nodes in the list, and returns the count. 
	def size(self):
		current = self.head
		count = 0
		while current:
			count += 1
			current = current.get_next()
		return count
		
	#Searches the list for the requested data. Returns the node. 
	def search(self, data):
		current = self.head
		found = False
		while current and found is False:
			if current.get_data() == data:
				found = True
			else:
				current = current.get_next()
		if current is None:
			raise ValueError("Data not in list")
		return current
	#Deletes a node from the list by taking its 'next' parameter
	#and assigning it to the previous node.
	def delete(self, data):
		current = self.head
		previous = None
		found = False
		while current and found is False:
			if current.get_data() == data:
				found = True
			else:
				previous = current
				current = current.get_next()
		if current is None:
			raise ValueError("Data not in list")
		if previous is None:
			self.head = current.get_next()
		else: 
			previous.set_next(current.get_next())