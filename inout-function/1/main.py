with open('input.txt', 'r') as file:
    wordlist = file.read().split()

def words_ending_in_ime(wordlist):
    return [word for word in wordlist if word.endswith('ime')]

def second_third_fourth_letters_are_ave(wordlist):
    return [word for word in wordlist if len(word) >= 4 and word[1:4] == 'ave']

def words_containing_letters(wordlist, letters):
    return [word for word in wordlist if any(letter in word for letter in letters)]

def percentage_of_words_containing_letters(wordlist, letters):
    containing_letters = words_containing_letters(wordlist, letters)
    return (len(containing_letters) / len(wordlist)) * 100 if len(wordlist) > 0 else 0

def words_with_no_vowels(wordlist):
    vowels = 'aeiou'
    return [word for word in wordlist if all(letter not in vowels for letter in word.lower())]

def words_containing_every_vowel(wordlist):
    vowels = 'aeiou'
    return [word for word in wordlist if all(vowel in word.lower() for vowel in vowels)]

result_a = words_ending_in_ime(wordlist)
result_b = second_third_fourth_letters_are_ave(wordlist)

letters_to_check = {'r', 's', 't', 'l', 'n', 'e'}
result_c = words_containing_letters(wordlist, letters_to_check)
result_d = percentage_of_words_containing_letters(wordlist, letters_to_check)
result_e = words_with_no_vowels(wordlist)
result_f = words_containing_every_vowel(wordlist)

with open('a.txt', 'w') as file:
    for i in result_a:
        file.write(f'{i}\n')
with open('b.txt', 'w') as file:
    for i in result_b:
        file.write(f'{i}\n')
with open('c.txt', 'w') as file:
    file.write(f'{len(result_c)}\n')
with open('d.txt', 'w') as file:
        file.write(f'{result_d}%\n')
with open('e.txt', 'w') as file:
    for i in result_e:
        file.write(f'{i}\n')
with open('f.txt', 'w') as file:
    for i in result_f:
        file.write(f'{i}\n')

