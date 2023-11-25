d = {
    'c1': 'Red',
    'c2': 'Green',
    'c3': None
}

d1 = {}

for k, v in d.items():
    if v != None:
        d1[k] = v

print(d1)
