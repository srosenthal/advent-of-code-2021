with open('input.txt') as f:
    prev_depth = None
    num_increases = 0
    for line in f.readlines():
        depth = int(line)
        if prev_depth is not None and depth > prev_depth:
            print(line + " increased!")
            num_increases += 1
        else:
            print(line)
        prev_depth = depth
    print("num increases: " + str(num_increases))
