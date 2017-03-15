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