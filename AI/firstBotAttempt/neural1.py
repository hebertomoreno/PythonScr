'''https://medium.com/technology-invention-and-more/how-to-build-a-simple-neural-network-in-9-lines-of-python-code-cc8f23647ca1#.ge7vzmd56
What is a Nueural Network?
	The human brain consists of 100 billion cells called
	neurons, connected together by synapses. If 
	sufficient synaptic inputs to a neuron fire, 
	that neuron will also fire. We call this process 
	"thinking". 
How do we teach our neuron to answer the question correctly?
	We will give each input a weight, which can be a positive
	or negative number. An input with a large positive weight
	or a large negative weight, will have a stron efffect on 
	the neuron's output. 

1. Take the inputs from a training set example, adjust them by the
weights, and pass them through a special formula to calculate the
neuron's output. 

2. Calculate the error, which is the difference between the neuron's 
output and the desired output in the training set example. 

3. Depending on the direction of the error, adjusts the weights
slightly. 

4. Repeat this process 10,000 times.

Special formula for calculating neuron's output:

Sigma weight[i] x input[i] = weight[1] x input[1] + weight[2] x input[2] + weight[3] x input[3]


Because we need this to be between 0 and 1, we normalize using the 
sigmoid function, which is 1/(1+e**(-x))
If plotted on a graph, the Sigoid function draws an S shaped curve.

So, by substituting the first equation into the second, we get:

	Output of neuron = 1/(1 + e ** -(Sigma weight[i] x input[i]))

During the training cycle, we adjust the weights. We use the "Error Weighted Derivative" formula:

	Adjust weights by = error 
''' 
from numpy import exp, array, random, dot

class NeuralNetwork():
	def __init__(self):
		# Seed the random number generator, so it generates the same numbers
		# every time the program runs.
		random.seed(1)

		# We model a single neuron, with 3 input connections and 1 
		# output connection. We assign random weights to a 3 x 1 matrix,
		# with values in the range -1 to 1 and mean 0.
		self.synaptic_weights = 2 * random.random((3,1)) - 1

	# The Sigmoid function, which describes an S shaped curve. 
	# We passs the weighted sum of the inputs through this function to
	# normalise them between 0 and 1. 
	def __sigmoid(self,x):
		return 1 / (1 + exp(-x))

	# The derivative of the Sigmoid function.
	# This is the gradient of the Sigmoid curve.
	# It indicates how confident we are about the existing weight. 
	def __sigmoid_derivative(self,x):
		return x * (1 - x)

	# We train the neural network through a process of trial and error. 
	# Adjusting the synaptic weights each time. 
	def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
		for iteration in xrange(number_of_training_iterations):
			# Pass the training set through our neural network ( a single neuron).
			output = self.think(training_set_inputs)

			# Calculate the error (The difference between the desired output and
			# the predicted output)
			error = training_set_outputs - output

			# Multiply the error by the input and again by the gradient of the Sigmoid curve. 
			# This means less confident weights are adjusted more. 
			#This means inputs, which are zero, do not cause changes to the weights. 
			adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))

			# Adjust the weights
			self.synaptic_weights += adjustment

	def think(self, inputs):
		# Pass inputs through our neural network (our single neuron).
		return self.__sigmoid(dot(inputs, self.synaptic_weights))

if __name__ == "__main__":

	#Initialise a single neuron neural network
	neural_network = NeuralNetwork()

	print " Random starting synaptic weights: "
	print neural_network.synaptic_weights

	# The training set. We have 4 examples, each consisting of 3 input values
	# and 1 output value. 
	training_set_inputs = array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
	#The '.T' function transposes the matrix from horizontal to vertical
	training_set_outputs = array([[0,1,1,0]]).T

	# Train the neural network using a training set. 
	# Do it 10,000 times and make small adjustments each time. 
	neural_network.train(training_set_inputs, training_set_outputs, 10000)

	print "New synaptic weights after training: "
	print neural_network.synaptic_weights

	# Test the neural network with a new situation.
	print "Considering new situation [1,0,0] -> ?"
	print neural_network.think(array([1,0,0]))