from matrixop import *
from neuralnet import *
import random

training_data = [[0,0],[1,0],[0,1],[1,1]]
targets = [[0],[1],[1],[0]]

nn = NeuralNetwork(2,3,1)

for i in range(1):
	print("iteration :",i)
	k = random.randint(0,3)
	inputs = training_data[k]
	answers = targets[k]
	nn.train(inputs,answers)

for i in range(len(training_data)):
	output= nn.feedforward(training_data[i])
	print(output)