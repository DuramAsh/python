class Wordplay:
	def __init__(self, words):
		self.words = words

	def words_with_length(self, length):
		return [word for word in self.words if len(word) == length]

	def starts_with(self, s):
		return [word for word in self.words if word[0] == s]

	def ends_with(self, s):
		return [word for word in self.words if word[-1] == s]

	def palindromes(self):
		return [word for word in self.words if word == word[::-1]]

	def only(self, L):
		return [word for word in self.words if set(word).issubset(set(L))]

	def avoids(self, L):
		return [word for word in self.words if set(word).isdisjoint(set(L))]
	
words = ['apple', 'нажалкабаннабаклажан', 'banana', 'orange', 'pear', 'grape', 'pineapple', 'kiwi', 'mango', 'peach', 'plum', 'apricot', 'avocado', 'blackberry', 'blueberry', 'cherry', 'coconut', 'fig', 'grapefruit', 'lemon', 'lime', 'melon', 'nectarine', 'papaya', 'raspberry', 'strawberry', 'watermelon']
w = Wordplay(words)
print(w.words_with_length(5))
print(w.starts_with('a'))
print(w.ends_with('e'))
print(w.palindromes())
print(w.only('bna'))
print(w.avoids('aep'))