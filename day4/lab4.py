from math import sqrt 

def max_div (number1, number2):
	while number2 != 0:
		rem = number1 % number2
		number1 = number2
		number2 = rem
		max_div(number1, number2)
	return(number1)


print max_div(1071, 462)
print max_div(30,25)


def primes():
	boolean_ary = [True] * 121
	for i in  range(2,12):
		if boolean_ary[i]:
			for j in range(i**2,121,i):
				boolean_ary[j] = False
	return [i for i,x in enumerate(boolean_ary) if (x==True & i>0)]


print primes()



