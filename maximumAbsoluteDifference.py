class Difference:
	def __init__(self, elements):
		self.elements = elements
		self.maximumDifference = 0
	def computeDifference(self):
		maxDif = 0
		for number in elements:
			for number2 in elements:
				if(elements.index(number) != elements.index(number2)):
					tempDif = abs(number - number2)
					maxDif = tempDif if tempDif > maxDif
		self.maximumDifference = maxDif

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)