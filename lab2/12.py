def solve(n, nums):
	return n in nums

n = int(input())
l = list(map(int, input().split()))

print(solve(n, l))