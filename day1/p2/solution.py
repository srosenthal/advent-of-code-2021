import more_itertools

depths = []
with open('input.txt') as f:
    for line in f.readlines():
        depths.append(int(line))

window_size = 3
prev_avg = None
num_increases = 0
for window in more_itertools.windowed(depths, n=window_size, step=1):
    avg = sum(window) / window_size

    if prev_avg is not None and avg > prev_avg:
        print(line + " increased!")
        num_increases += 1
    else:
        print(line)
    prev_avg = avg
print("num increases: " + str(num_increases))
