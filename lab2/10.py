def solve(s, n):
    return s * n if len(s) < 2 else s[:2] * n

s = input()
n = int(input())

print(solve(s, n))
