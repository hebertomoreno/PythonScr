#Simple Binary Tree

class BinaryTree():
	def __init__(self,rootid):
		self.left = None
		self.right = None
		self.rootid = rootid
	def getLeftChild(self):
		return self.left
	def getRightChild(self):
		return self.right
	def setNodeValue(self, value):
		self.rootid = value
	def getNodeValue(self):
		return self.rootid

	def insertRight(self, newNode):
		if self.right == None:
			self.right = BinaryTree(newNode)
		else: 
			tree = BinaryTree(newNode)
			tree.right = self.right
			self.right = tree
	def insertLeft(self, newNode):
		if self.left == None:
			self.left = BinaryTree(newNode)
		else:
			tree = BinaryTree(newNode)
			self.left = tree
			tree.left = self.left
def printTree(tree):
	if tree != None:
		print(tree.getNodeValue)
		printTree(tree.getLeftChild())
		printTree(tree.getRightChild())
	else: 
		return 

# test Tree

def testTree():
	myTree = BinaryTree('Maud')
	myTree.insertLeft('Bob')
	myTree.insertRight('Tony')
	myTree.insertRight('Steven')
	myTree.insertLeft('Random Character')
	printTree(myTree)

testTree()