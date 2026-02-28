def print_odd_numbers(a, b):
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        if i % 2 == 1:
            print(i, end=" ")
    print()