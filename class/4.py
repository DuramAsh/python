class Time:
	def __init__(self, seconds):
		self.seconds = seconds
	
	def convert_to_minutes(self):
		return f'{self.seconds // 60}:{self.seconds % 60}'
	
	def convert_to_hours(self):
		return f'{self.seconds // 3600}:{self.seconds % 3600 // 60}:{self.seconds % 60}'

t = Time(80000)
print(t.convert_to_minutes())
print(t.convert_to_hours())