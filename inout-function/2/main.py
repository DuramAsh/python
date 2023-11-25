def square(a):
	return a * a

with open('input.txt', 'r') as file:
    side = int(file.read().split()[0])

with open('output.txt', 'w') as file:
	file.write(f'{square(side)}\n')
