def sum_range(start, end):
    if start > end:
        start, end = end, start

    sum = 0
    for i in range (start, end + 1):
        sum += i
    return sum

a, b = map(int, input().split())
print(sum_range(a, b))