def solve(nums):
	cnt = 0
	for i in nums:
		if i == 4:
			cnt += 1
	return cnt


nums = list(map(int, input().split()))
print(solve(nums))