#Jonathan and Michelle: Task 1

def is_triangle(num1, num2, num3):
	if (num1>num2+num3) | (num2>num1+num3) | (num3>num1+num2):
		print "No"
	else:
		print "Yes"
		
def prompt():
	num1 = raw_input("Give me the first number: ")
	num1 = int(num1)
	num2 = raw_input("Give me the second number: ")
	num2 = int(num2)
	num3 = raw_input("Give me the third number: ")
	num3 = int(num3)
	is_triangle(num1, num2, num3)