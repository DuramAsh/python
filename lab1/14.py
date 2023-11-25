def remove_every_third(numbers):
    count = 0
    while len(numbers):
        if count % 3 == 0:
            if len(numbers) >= 3:
                n = numbers.pop(2)
                print("", n)
            else:
                n = numbers.pop()
                print("", n)
        else:
            numbers.append(numbers.pop(0))
        count += 1

numbers = list(map(int, input().split()))
remove_every_third(numbers)
