def solve(l, f):
    return f'{f} {l}'


with open('input.txt', 'r') as file:
    last_name, first_name = file.read().split()

with open('output.txt', 'w') as file:
    file.write(f'{solve(last_name, first_name)}\n')
