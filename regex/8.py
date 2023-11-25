import re

text = 'Python Exercises, PHP exercises.'
print(re.sub(r'[\s,.]', ':', text))