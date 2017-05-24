class Stack: 
	def __init__(self):
		self.items = []
	def push(self, item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def is_empty(Self):
		return (self.items == [])
	def peek(self):
		return self.items[-1]