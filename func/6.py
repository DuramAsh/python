def bank(a, years):
    interest = 0.1
    return a * (1 + interest) ** years


a, years = map(int, input().split())
print(bank(a, years))
