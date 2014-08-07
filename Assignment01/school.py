from collections import OrderedDict

class School():
	def __init__(self, school_name):
		self.school_name = school_name
		self.db = {}


	def add(self, name, grade):
		if grade in self.db:
			self.db[grade].add(name)
		else:
			self.db[grade] = {name}

	def grade(self, grade):
		if grade not in self.db.keys():
			return None
		else:
			return self.db.get(grade)
		print self.db.keys

	def sort(self):
		new_dic = self.db
		new_dic = OrderedDict(sorted(self.db(), key=lambda x: x[1]))



    #def test_sort_school(self):
     #   self.school.add("Jennifer", 4)
      #  self.school.add("Kareem", 6)
       # self.school.add("Christopher", 4)
        #self.school.add("Kyle", 3)
        #sorted_students = {
         #   3: ("Kyle",),
          #  4: ("Christopher", "Jennifer",),
           # 6: ("Kareem",)
       # }
        #self.assertEqual(sorted_students, self.school.sort())

school = School("RANDOM")
school.add("James", 2)
school.add("Blair", 2)
school.add("Paul", 2)
school.add("Maria", 1)
school.add("Andy", 3)
test = school.db
print len(test)
print test.keys()
x = test.values()
y = x[1] 
print y.sorted()







		

