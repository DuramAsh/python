import re
words = ['right', 'ok', 'eleven', 'big', 'nose', 'lucky', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

for word in words:
	if re.search(r'[rstlne]', word):
		print(word)