## First exercise
class Clock():
	def __init__(self, hours, minutes=0):
		self.hours = hours
		self.minutes = minutes
	
	@classmethod
	def at (cls, hours, minutes=0):
		return cls(hours, minutes)

test = Clock(8,35)
print test.at()


### 3

