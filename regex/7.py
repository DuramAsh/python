import re

words = ['rr', 'no', 'kk', 'ball', 'ptr', 'always', 'aeiadssou', 'elements','bongo', 'eleven', 'bongoes', 'bongoest']

for word in words:
	if re.search(r'^[ae]', word):
		print(word)