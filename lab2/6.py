def solve(s):
    return s if s.lower().startswith("is") else 'Is' + s

print(solve(input()))