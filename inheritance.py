class Student(person):
	'''The constructor for a class that inherits from another class can initialize with 
	a different set of values from its parent.'''
	def __init__(self, firstName, lastName, idNum, scores):
		self.firstName = firstName
		self.lastName = lastName
		self.id = idNum
		self.scores = scores
	def calculate(self):
		avg = 0
		for score in self.scores:
			avg += score
		avg = avg/len(self.scores)
		return avg