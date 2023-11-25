def solve(number):
    difference = abs(number - 17)
    return 2 * difference if number > 17 else difference

print(solve(int(input())))
