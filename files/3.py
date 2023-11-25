import re

a, b, c, d = [], [], 0, []

with open('random_text.txt', 'r') as f:
    rows = f.readlines()

    for row in rows:
        row.replace('\n', '')
        row = row.split()

        for r in row:
            if re.match(r'^[a-zA-Z]{4}$', r):
                a.append(r)
            if re.match(r'^th', r):
                b.append(r)
            if re.match(r'^[a-zA-Z]{5}$', r):
                c += 1
            if re.match(r'^\d+$', r):
                d.append(r)


print('\nWords consisting of 4 letters:')
print(*a)
print("\nWords starting with 'th':")
print(*b)
print(f"\nAmount of words which have 5 letters: {c}")
print("\nNumbers in the text:")
print(*d)
