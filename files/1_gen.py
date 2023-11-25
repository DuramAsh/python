import random

with open('grades.txt', 'w') as f:
    letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    surnames = ['Washington', 'Smith', 'Jordan', 'Blossom', 'Pary', 'Nicholas']
    for i in range(100):
        name, a, b, c = letters[random.randint(0, len(letters) - 1)] + random.choice(surnames), random.randint(
            0, 101), random.randint(0, 101), random.randint(0, 101)
        f.write(f'{name} {a} {b} {c}\n')
