def perimeter(a, b):
    return 2*(a + b)


with open('input.txt', 'r') as file:
    length, width = map(int, file.read().split())

with open('output.txt', 'w') as file:
    file.write(f'{perimeter(length, width)}\n')
