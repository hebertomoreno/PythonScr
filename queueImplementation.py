def Queue:
	def __init__(self):
		self.length = 0
		self.head = None

	def is_empty(self):
		return (self.length == 0)

	def insert(self, cargo):
		node = Node(cargo)
		node.next = None
		if self.head == None:
			# if list is empty then the new node goes first
			self.head = node
		else:
			# find the last node in the list
			last = self.head
			while last.next: 
				last = last.next
			# append the new node
			last.next = node
		self.length = self.length + 1

	def remove(self):
		cargo = self.head.cargo
		self.head = self.head.next
		self.length = self.length -1
		return cargo
class ImprovedQueue:
	def __init__(self):
		self.length = 0
		self.head = None
		self.last = None
	def is_empty(self):
		return (self.length == 0)
	def insert(self, cargo):
		node = Node(cargo)
		node.next = None
		if self.length == 0:
			self.head = self.last = node
		else:
			last = self.last
			last.next = node
			self.last = node
		self.length = self.length + 1
	def remove(self):
		cargo = self.head.cargo
		self.head = self.head.next
		self.length = self.length - 1
		if self.length == 0:
			self.last = None
		return cargo