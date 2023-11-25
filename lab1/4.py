def sum_of_n_positive_integers(n):
	return sum([i for i in range(1, n+1)])

a = int(input())
print(sum_of_n_positive_integers(a))
