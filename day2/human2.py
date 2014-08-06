class Parent():
	def __init__(self, sex, firstname, lastname):
		self.sex = sex
		self.firstame = firstname
		self.lastname = lastname
		self.kids = []
		
	def role(self):
		if self.sex == "Male": 
			return "Father"
		else:
			return "Mother"
			
	def have_child(self, name):
		child = Child(name, self)
		print self.firstname + "is having a child named" + child
		print "They will make a very good" + self.role()
		selfkids.append(child) 
			
	def list_children(self):
		for kid in self.kids:
			print "I am the " + self.role() + "of " + kid.name()
			
class Child():
	def __init__(self, firstname, parent):
		self.parent = parent
		self.lastname  = parent.lastname
		self.firstname = firstname
		
	def set_name(self, new_firsnt_name, new_last_name):
		self.firstname = new_first_name
		self.lastname = new_last_name
		
	def name(self):
		return "%s %s" % (self.firstname, self.lastname)
		
	def introduce(self):
		return "Hi I'm %s %s" % (self.firstname, self.lastname)
		
mom = Parent("Female", "Jane", "Smith")
mom.list_children()
jill = mom.have_child("Jill")
print jill.introduce()
jack = mom.have_child("Jack")
print jack.introduce()
mom.list_children()