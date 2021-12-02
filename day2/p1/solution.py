with open('input.txt') as f:
    dx = 0
    depth = 0

    for line in f.readlines():
        direction, num = line.split()
        num = int(num)
        if direction == 'forward':
            dx += num
        elif direction == 'backward':
            dx -= num
        elif direction == 'down':
            depth += num
        elif direction == 'up':
            depth -= num

    print("dx = {}, depth = {}, product = {}".format(dx, depth, dx * depth))
