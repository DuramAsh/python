def is_vowel(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter.lower() in vowels

print(is_vowel(input()))