import math

def area(r):
	return math.pi * r ** 2

with open('input.txt', 'r') as file:
    radius = int(file.read().split()[0])

with open('output.txt', 'w') as file:
	file.write(f'{area(radius)}\n')
