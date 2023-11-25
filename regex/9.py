import re

text = 'Python Exercises, PHP exercises. This is a long string with some words that are 3 4 or 5 characters long'

words = text.split()

for word in words:
	if re.search(r'^.{3,5}$', word):
		print(word)