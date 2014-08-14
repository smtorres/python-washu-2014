
def Bubble(vector_numbers):
	start = 0
	for j in range(len(vector_numbers)):
		mini = min(vector_numbers[j:len(vector_numbers)])
		min_num = vector_numbers[j:len(vector_numbers)].index(mini)
		if vector_numbers[j] >= mini:
			vector_numbers[j], vector_numbers[(j+min_num)] = vector_numbers[(j+min_num)], vector_numbers[j]
		else: 
			pass
	return vector_numbers


def test_sort(x):
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

x = [1,4,2,8,7,6,4,9]
print Bubble(x)
print test_sort(x)
