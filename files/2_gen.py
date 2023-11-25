import random

with open('logfile.txt', 'w') as f:
    names = ['Van', 'Blake', 'Turner', 'Jake', 'Mike', 'Jennie', 'Bob']
    surnames = ['Washington', 'Smith', 'Jordan', 'Blossom', 'Pary', 'Nicholas']

    for i in range(100):
        name = random.choice(names) + ' ' + random.choice(surnames)
        h1 = random.randint(1, 23)
        if h1 < 10:
            h1 = '0' + str(h1)
        h2 = random.randint(int(h1), 23)
        if h2 < 10:
            h2 = '0' + str(h2)
        m1, m2 = random.randint(1, 59), random.randint(1, 59)
        if m1 < 10:
            m1 = '0' + str(m1)
            if m2 < 10:
                m2 = '0' + str(m2)
        f.write(f'{name}, {h1}:{m1}, {h2}:{m2}\n')
