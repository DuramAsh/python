def determine_collectible_type(object):
	if isinstance(object, list):
		return "list"
	elif isinstance(object, tuple):
		return "tuple"
	elif isinstance(object, set):
		return "set"

a = []
b = set()
c = ()
print(determine_collectible_type(a))
print(determine_collectible_type(b))
print(determine_collectible_type(c))