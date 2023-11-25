def is_even(n):
	return n % 2 == 0

n = int(input())

if is_even(n):
	print(f"Number {n} is even")
else:
	print(f"Number {n} is odd")