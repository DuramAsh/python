from datetime import datetime, timedelta

cnt = 0
with open('logfile.txt', 'r') as f:
    rows = f.readlines()

    for row in rows:
        row = row.replace(' ', '')
        row = row.split(',')

        start, end = datetime.strptime(
            row[1], "%H:%M"), datetime.strptime(row[2][:-1], "%H:%M")
        diff = end - start
        if diff >= timedelta(hours=1):
            cnt += 1
            print(row[0])

print(cnt)
