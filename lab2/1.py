from datetime import datetime

def solve(date1, date2):
    dt1 = datetime(*date1)
    dt2 = datetime(*date2)

    return (dt2 - dt1).days

    print("The difference in days is:", difference)

date1 = (2014, 7, 2)
date2 = (2014, 7, 11)

print(solve(date1, date2), 'days')