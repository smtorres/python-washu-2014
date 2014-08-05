## First exercise
class Clock():
	def __init__(self, hours, minutes=0):
		self.hours = hours
		self.minutes1 = hours*60
		self.minutes2 = minutes
		

	@classmethod
	def at(cls,hours,minutes=0):
		return cls(hours, minutes)
		#print "%02d:%02d" % (hours, minutes)
		#return hours*60 + minutes
		#return cls(hours, minutes)
		#return "%02d:%02d"	% (hour2, min2)
		#return(time)
		
	def __str__(self):
	#	time = at(self.hours, self.minutes2)
	#	hour2 = time/60
	#	min2 = time % 60
		return "%02d:%02d" % (self.hours, self.minutes2)
		
	def __add__(self, other):
		time = self.minutes1 + (self.minutes2 + other)
		hour2 = time/60
		min2 = time % 60
		if hour2>23:
			hour2=hour2-24
		return "%02d:%02d" % (hour2, min2)
		
	def __sub__(self, other):
		time = self.minutes1 - (self.minutes2 + other)
		hour2 = time/60
		min2 = time % 60
		return "%02d:%02d" % (hour2, min2)
		
	def _eq_ (self, other):
		time = self.hours*60 + self.minutes2
		return time==other
		
		
clock = Clock.at(10) + 61
print clock
clock2 = Clock.at(10) - 91
print clock2
clock3 = Clock.at(23,30) + 60
print clock3

clock4 = Clock.at(15, 37)
clock5 = Clock.at(15, 37)
print clock4==clock5
print clock4
print clock5
