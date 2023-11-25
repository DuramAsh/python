import re

words = ['rr', 'no', 'kk', 'ball', 'ptr', 'always', 'aeiadssou', 'bongo', 'bongoes', 'bongoest']

for word in words:
	if re.search(r'a', word) and re.search(r'e', word) and re.search(r'i', word) and re.search(r'o', word) and re.search(r'u', word):
		print(word)