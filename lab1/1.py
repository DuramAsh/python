def get_object_identity(object):
	return id(object)

a = 5
print(get_object_identity(a))