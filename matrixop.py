import random
from pandas import *

def matrix_initialize(rows,columns):
	m = [[0 for i in range(columns)]for j in range(rows)]
	return m

def matrix_random_initialize(rows,columns):
	m = [[0 for i in range(columns)]for j in range(rows)]
	for i in range(rows):
		for j in range(columns):
			m[i][j] = random.uniform(-1,1)
	return m

def matrix_add(matrix,m):
	result = [[0 for i in range(len(matrix[0]))]for j in range(len(matrix))]
	if type(m) != type(matrix):
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				result[i][j] = m+matrix[i][j]
	else:
		if len(matrix[0])!=len(m[0]) or len(matrix)!=len(m):
			print("Their dimensions donot match")
			return -1
		else:
			for i in range(len(matrix)):
				for j in range(len(matrix[0])):
					result[i][j] = matrix[i][j]+m[i][j]
	return result

def matrix_sub(matrix,m):
	result = [[0 for i in range(len(matrix[0]))]for j in range(len(matrix))]
	if type(m) != type(matrix):
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				result[i][j] = matrix[i][j]-m
	else:
		if len(matrix[0])!=len(m[0]) or len(matrix)!=len(m):
			print("Their dimensions donot match")
			return -1
		else:
			for i in range(len(matrix)):
				for j in range(len(matrix[0])):
					result[i][j] = matrix[i][j]-m[i][j]
	return result

def matrix_scalar_mul(matrix,m):
	result = [[0 for i in range(len(matrix[0]))]for j in range(len(matrix))]
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			result[i][j] = m*matrix[i][j]
	return result

def matrix_dot_mul(matrix,m):
	if len(matrix[0])!=len(m):
		print("They donot have the right dimensions")
		return -1
	else:
		result = [[0 for i in range(len(m[0]))]for j in range(len(matrix))]
		for i in range(len(matrix)):
			for j in range(len(m[0])):
				for k in range(len(m)):
					result[i][j] += matrix[i][k]*m[k][j]
		return result

def matrix_transpose(matrix):
	result = [[0 for i in range(len(matrix))]for j in range(len(matrix[0]))]
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			result[j][i] = matrix[i][j]
	return result

def print_matrix(matrix):
	if type(matrix)!=type([]):
		print(-1)
	else:
		print(DataFrame(matrix))

def matrix_mapper(matrix,func):
	result = [[0 for i in range(len(matrix[0]))]for j in range(len(matrix))]
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			result[i][j] = func(matrix[i][j])
	return result

def arr_to_mat(arr):
	l = []
	l.append(arr)
	return (matrix_transpose(l))

def mat_to_arr(matrix):
	result = []
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			result.append(matrix[i][j])
	return result

def matrix_hadamard(matrix,m):
	if len(matrix)!= len(m) or len(matrix[0])!=len(m[0]):
		print("The dimensions donot match")
		return -1
	result = [[0 for i in range(len(matrix[0]))]for j in range(len(matrix))]
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			result[i][j] = matrix[i][j]*m[i][j]
	return result