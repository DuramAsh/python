class Product:
	def __init__(self, name, amount, price):
		self.name = name
		self.amount = amount
		self.price = price
	
	def get_price(self, items):
		if items < 10:
			return self.price * items
		elif items < 100:
			return self.price * items * 0.9
		else:
			return self.price * items * 0.8
	
	def make_purchase(self, items):
		self.amount -= items

p = Product('Apple', 100, 10)
print(p.get_price(5))
print(p.get_price(50))
print(p.get_price(500))
print(p.amount)
p.make_purchase(10)
print(p.amount)