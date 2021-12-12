with open('input.txt') as f:
    dx = 0
    depth = 0
    aim = 0

    for line in f.readlines():
        direction, num = line.split()
        num = int(num)
        if direction == 'forward':
            dx += num
            depth += (aim * num)
        elif direction == 'backward':
            dx -= num
            depth -= (aim * num)
        elif direction == 'down':
            aim += num
        elif direction == 'up':
            aim -= num

    print("dx = {}, depth = {}, product = {}".format(dx, depth, dx * depth))
