from matrixop import *
import math

def sigmoid(x):
	return (1/(1+math.exp(-x)))

def dsigmoid(x):
	return (x*(1-x))

class NeuralNetwork:
	def __init__(self, input_nodes,hidden_nodes,output_nodes):
		self.input_nodes = input_nodes
		self.hidden_nodes = hidden_nodes
		self.output_nodes = output_nodes

		self.weights_ih = matrix_random_initialize(hidden_nodes,input_nodes)
		self.weights_ho = matrix_random_initialize(output_nodes,hidden_nodes)

		self.bias_h = matrix_random_initialize(hidden_nodes,1)
		self.bias_o = matrix_random_initialize(output_nodes,1)
		self.learning_rate = 0.1

	def feedforward(self,inpu):
		#generating first hidden outputs
		inputs = arr_to_mat(inpu)
		hidden = matrix_dot_mul(self.weights_ih,inputs)
		hidden = matrix_add(hidden,self.bias_h)
		#activation function
		hidden = matrix_mapper(hidden,sigmoid)

		#output layer 
		output = matrix_dot_mul(self.weights_ho,hidden)
		output = matrix_add(output,self.bias_o)
		output = matrix_mapper(output,sigmoid)
		# output = mat_to_arr(output)
		return output

	def train(self, inpu, answer):
		#verified
		inputs = arr_to_mat(inpu)
		answers = arr_to_mat(answer)
		inputs_T = matrix_transpose(inputs)
		# output = self.feedforward(inputs)
		hidden = matrix_dot_mul(self.weights_ih,inputs)
		hidden = matrix_add(hidden,self.bias_h)
		#activation function
		hidden = matrix_mapper(hidden,sigmoid)
		print(hidden,"hidden")
		output = matrix_dot_mul(self.weights_ho,hidden)
		output = matrix_add(output,self.bias_o)
		output = matrix_mapper(output,sigmoid)


		#confusing
		#calculate error
		#error = answer - target
		error_o = matrix_sub(answers, output) #done
		print(error_o,output)
		#calculate gradient
		gradient = matrix_mapper(output,dsigmoid)
		print("gradient-1",gradient)
		gradient = matrix_hadamard(gradient,error_o)
		print("gradient",gradient)
		gradient = matrix_scalar_mul(gradient,self.learning_rate)
		print("gradient2",gradient)
		hidden_T = matrix_transpose(hidden)
		print("hidden_T",hidden_T)
		weights_ho_deltas = matrix_dot_mul(gradient,hidden_T)
		print("weights_ho_deltas",weights_ho_deltas)
		print(self.weights_ho,"weights_ho")
		self.weights_ho = matrix_add(self.weights_ho,weights_ho_deltas)
		print(self.weights_ho,"weights_ho2")
		self.bias_o = matrix_add(self.bias_o,gradient)

		
		weights_ho_t = matrix_transpose(self.weights_ho)
		print(weights_ho_t,error_o,"error_h_previous")
		error_h = matrix_dot_mul(weights_ho_t,error_o)
		print("error_h",error_h)
		hidden_gradient = matrix_mapper(hidden,dsigmoid)
		hidden_gradient = matrix_hadamard(hidden_gradient,error_h)
		hidden_gradient = matrix_scalar_mul(hidden_gradient,self.learning_rate)
		
		weights_ih_deltas = matrix_dot_mul(hidden_gradient,inputs_T)
		self.weights_ih = matrix_add(self.weights_ih,weights_ih_deltas)

		self.bias_h = matrix_add(self.bias_h,hidden_gradient)