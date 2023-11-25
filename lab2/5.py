def solve(numbers):
    total_sum = sum(numbers)
    return 3 * total_sum if numbers[0] == numbers[1] == numbers[2] else total_sum

print(solve(list(map(int, input().split()))))