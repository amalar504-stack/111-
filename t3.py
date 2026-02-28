def draw_line(length, direction, symbol):
    if direction == 'h':
        print(symbol * length)
    else:
        for i in range(length):
            print(symbol)