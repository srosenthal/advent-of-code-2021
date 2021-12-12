# Read the input file
lines = []
with open('input.txt') as f:
    for line in f.readlines():
        line = line.strip('\n')
        lines.append(line)

def print_grid(grid):
    pass
    # skipping this for the real input because it's too noisy
    #for row in grid:
    #    print("".join([str(v) for v in row]).replace('0', '.'))

N = 1000
grid = [[0]*N for i in range(N)]
for line in lines:
    start, end = line.split(' -> ')
    print("start, end = {}, {}".format(start, end))
    start_x, start_y = start.split(',')
    end_x, end_y = end.split(',')

    start_x = int(start_x)
    start_y = int(start_y)
    end_x = int(end_x)
    end_y = int(end_y)

    # identify the increment between points (0, +1 or -1)
    dx, dy = 0, 0
    if end_x != start_x:
        dx = int((end_x - start_x) / abs(end_x - start_x))
    if end_y != start_y:
        dy = int((end_y - start_y) / abs(end_y - start_y))

    print("processing line {}".format(line))
    print("dx, dy = {}, {}".format(dx, dy))
    x, y = start_x, start_y
    while True:
        print("incrementing (x,y) = {}, {}".format(x, y))
        grid[y][x] += 1
        if x == end_x and y == end_y:
            break
        x += dx
        y += dy

    print_grid(grid)
    print("-----")

count = 0
for row in grid:
    for val in row:
        if val >= 2:
            count += 1

print("points with overlap >= 2: {}".format(count))
