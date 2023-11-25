cnt = 0

with open('grades.txt', 'r') as f:
    rows = f.readlines()

    for row in rows:
        row = row.split()
        a, b, c = int(row[1]), int(row[2]), int(row[3])
        if a >= 50 and b >= 50 and c >= 50:
            cnt += 1

print(cnt)
