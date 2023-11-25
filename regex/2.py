import re
words = ['bave', 'raven', 'crow', 'magazine', 'save', 'have', 'wave', 'should', 'go', 'miss']
for word in words:
	if re.search(r'^.ave.*$', word):
		print(word)