import random
from time import sleep
import matplotlib.pyplot as plt

width = 1000
height = 1000
#activation function
def activation(number):
	if number>0:
		return 1
	else:
		return -1

#simple perceptron
class Perceptron:
	"""docstring for Perceptron"""
	def __init__(self):
		#initialize the weights
		self.weights = [0]*3
		self.lr = 0.001
		for i in range(len(self.weights)):
			self.weights[i] = random.uniform(-1,1)

	def guess(self,inputs):
		gues = 0
		for i in range(len(self.weights)):
			gues += self.weights[i]*inputs[i]
		return activation(gues)

	def train(self,inputs,target):
		error = target-self.guess(inputs)
		for i in range(len(self.weights)):
			self.weights[i] += error*inputs[i]*self.lr

	def guessY(self, value):
		weights = self.weights
		return -1*((weights[2]/weights[1]) +(weights[0]/weights[1])*value)

def f(x):
	return 0.3*x+0.2

class Point:
	def __init__(self):
		self.x = random.uniform(0,width)
		self.y = random.uniform(0,height)
		self.bias = 1
		self.label = 0
		if self.y > f(self.x):
			self.label = 1
		else:
			self.label = -1

	def specific_values(self,x,y):
		self.x = x
		self.y = y

#setup
p = Perceptron()

no_of_points = 500

points = [0]*no_of_points
for i in range(no_of_points):
	points[i] = Point()

while True:
	for i in range(no_of_points):
		inputs = [points[i].x,points[i].y,points[i].bias]
		p.train(inputs,points[i].label)

		gues = p.guess(inputs)
		if (gues == points[i].label):
			plt.plot(points[i].x,points[i].y,'bo')
		else :
			plt.plot(points[i].x,points[i].y,'ro')
	x1 = 0
	y1 = f(0)
	x2 = width
	y2 = f(width)
	point1 = Point()

	plt.axline((x1,y1),(x2,y2))
	plt.show(block = False)

	point1 = Point()
	point2 = Point()
	point1.specific_values(0,p.guessY(0))
	point2.specific_values(50,p.guessY(50))

	plt.axline((point1.x,point1.y),(point2.x,point2.y))
	plt.pause(3)
	plt.close()