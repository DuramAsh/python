import math


def square(a):
    return (a * 4, a * a, a * math.sqrt(2))


length = int(input())
print(*square(length))
