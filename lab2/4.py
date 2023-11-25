def solve(number):
    return abs(1000 - number) <= 100 or abs(2000 - number) <= 100

print(solve(int(input())))