#!/usr/bin/env
import timeit
from random import *
import matplotlib.pyplot as plt

def measureTime(a,x):
    start = timeit.time.clock() 
    a(x)
    elapsed = timeit.time.clock()
    elapsed = elapsed - start
    return elapsed


def MinSort(vector_numbers):
	start = 0
	for j in range(len(vector_numbers)):
		mini = min(vector_numbers[j:len(vector_numbers)])
		min_num = vector_numbers[j:len(vector_numbers)].index(mini)
		if vector_numbers[j] >= mini:
			vector_numbers[j], vector_numbers[(j+min_num)] = vector_numbers[(j+min_num)], vector_numbers[j]
		else: 
			pass
	return vector_numbers


def Bubble(x):
	n = range(len(x))
	n_rev = n[::-1]
	n_rev = n_rev[:-1]
	for i in n:
		swap = False
		for j in n_rev:
			if x[j] < x[j-1]:
				x[j], x[j-1] = x[j-1], x[j]
				swap = True 
		if not swap:
			break
		else:
			pass
	return x

def timeTest():
	sample = []
	BubbleTime = []
	MinSortTime = []
	for len_vector in range(2,5):
		n = randrange(1,1234567)
		seed((len_vector * n))
		numbersBubble = [randrange(-1000,1000) for i in xrange(len_vector)]
		seed((len_vector * n))
		numbersMinSort = [randrange(-1000,1000) for i in xrange(len_vector)]
		sample.append(len_vector)
		BubbleTime.append(measureTime(Bubble, numbersBubble)) 
		MinSortTime.append(measureTime(MinSort, numbersMinSort))
	return [sample, BubbleTime, MinSortTime]


x = [1,4,2,8,7,6,4,9]
print measureTime(Bubble, x)
x = [1,4,2,8,7,6,4,9]
print measureTime(MinSort, x)
time_test = timeTest()

graph = timeTest()
length_vector = graph[0]
Bubble_series = graph[1]
MinSort_series = graph[2]


# Plots
plt.plot(length_vector, Bubble_series, 'r--', length_vector, MinSort_series, 'bs')
plt.show()
