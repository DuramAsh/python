import re

words = ['time', 'lime', 'dime', 'mime', 'crime', 'grime', 'slime', 'chime', 'prime', 'sublime', 'thyme', 'rhyme']

for word in words:
    if re.search(r'ime$', word):
        print(word)