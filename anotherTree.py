class Tree:
	def __init__(self, cargo, left=None, right=None):
		self.cargo = cargo
		self.left = left
		self.right = right
	def __str__(self):
		return str(self.cargo)

def total(tree):
	if tree == None: return 
	return total(tree.left) + total(tree.right) + tree.cargo

def print_tree(tree):
	if tree == None: return
	print (tree.cargo, end = " ") 
	print_tree(tree.left)
	print_tree(tree.right)
def print_tree_postorder(tree):
	if tree == None: return
	

tree = Tree('+',Tree(1), Tree('*', Tree(2), Tree(3)))
print_tree(tree)