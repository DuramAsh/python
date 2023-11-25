import re
words = ['right', 'ok', 'eleven', 'big', 'nose', 'lucky', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

count = 0
for word in words:
	if re.search(r'[rstln]', word):
		count += 1

percentage = count/len(words) * 100
print(percentage, '%')
