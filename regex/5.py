import re

words = ['rr', 'no', 'kk', 'ball', 'ptr', 'always']
for word in words:
	if not re.search(r'[aeiou]', word):
		print(word)