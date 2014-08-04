def binarify(num): 	
	if num<=0: return '0'
	power=0
	while num % 2**power<num:
		y = num % 2**power
		power = power + 1
		x = power -1
	length = range(0, power)
	coefs = length[::-1]
	digits = length
	for i in coefs:
		temp_power = 2**i
		bin_num = num / temp_power
		digits[i] = str(num / temp_power)
		num = num % temp_power
	digits = digits[::-1]
	
	return ''.join(digits)

def int_to_base(num, base):
	"""convert positive integer to a string in any base"""
	if num<=0:  return '0' 
  	power=0
	while num % base**power<num:
		y = num % base**power
		power = power + 1
		x = power -1
	length = range(0, power)
	coefs = length[::-1]
	digits = length
	for i in coefs:
		temp_power = base**i
		bin_num = num / temp_power
		digits[i] = str(num / temp_power)
		num = num % temp_power
	digits = digits[::-1]
  
	return ''.join(digits)

def base_to_int(string, base):
  """take a string-formatted number and its base and return the base-10 integer"""
  if string=="0" or base <= 0 : return 0 
  result = 0 
  return result 

def flexibase_add(str1, str2, base1, base2):
  """add two numbers of different bases and return the sum"""
  result = int_to_base(tmp, base1)
  return result 

def flexibase_multiply(str1, str2, base1, base2):
  """multiply two numbers of different bases and return the product"""
  result = int_to_base(tmp, base1)
  return result 

def romanify(num):
  """given an integer, return the Roman numeral version"""
  result = ""
  return result