class Investment:
	def __init__(self, principal, interest):
		self.principal = principal
		self.interest = interest
	
	def value_after(self, n):
		return self.principal * (1 + self.interest) ** n
	
	def __str__(self):
		return f'Principal - ${self.principal:.2f}, Interest rate - {self.interest * 100:.2f}%'
	
i = Investment(1000, 0.0512)
print(i)
print(i.value_after(5))
print(i.value_after(10))
print(i.value_after(20))