def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
        return 'Unknown operation'


a, b = map(int, input().split())
operation = input()

print(calculate(a, b, operation))
