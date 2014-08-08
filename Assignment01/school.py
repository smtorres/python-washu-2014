from collections import OrderedDict

class School():
	def __init__(self, school_name):
		self.school_name = school_name
		self.db = {}

		# Function that adds values and keys to a dictionary. Keys are school grades and each can take as value the name of a kid belonging to that grade.
		# It returns a dictionary with the name of the keys
	def add(self, name, grade):
		if grade in self.db:
			self.db[grade].add(name)
		else:
			self.db[grade] = {name}

		# Function that takes as input Grade and delivers the names of the kids that belong to that group.
	def grade(self, grade):
		if grade not in self.db.keys():
			return None
		else:
			return self.db.get(grade)
		print self.db.keys

		# Function that sorts and converts the values of the dictionary from sets to tuples.
	def sort(self):
		new_dic = self.db
		for i in range(0, len(new_dic)):
				Key = new_dic.keys()[i]
				Value = new_dic.values()[i]
				Value = list(Value)
				Value = tuple(Value)
				new_dic[Key] = Value 
				print new_dic.values
		return new_dic













		

