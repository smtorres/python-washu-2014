class School():
	def __init__(self, school_name):
		self.school_name = school_name
		self.db = {}
		self.dict = {}


	def add(self, name, grade):
		self.dict = {name}
		if name in self.db:
			self.db[grade].add(name)
		else:
			temp_dict = {grade : self.dict}
	 		self.db.update(temp_dict)


school = School("Haleakala Hippy School")
print school.db
school.add("Aimee", 2)
school.add("Mark", 3)
school.add("Sophie", 4)
print school.db




		

