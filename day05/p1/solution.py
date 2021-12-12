# Read the input file
lines = []
with open('input.txt') as f:
    for line in f.readlines():
        line = line.strip('\n')
        lines.append(line)

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

    # order the start & end
    start_x, end_x = min(start_x, end_x), max(start_x, end_x)
    start_y, end_y = min(start_y, end_y), max(start_y, end_y)

    dx = end_x - start_x
    dy = end_y - start_y
    if not (dx == 0 or dy == 0):
        print("skipping diagonal line...")
        continue

    print("start_x, start_y, end_x, end_y = {}, {}, {}, {}".format(start_x, start_y, end_x, end_y))

    print("processing line {}".format(line))
    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            print("incrementing (x,y) = {}, {}".format(x, y))
            grid[y][x] += 1

    #for row in grid:
    #    print("".join([str(v) for v in row]))

count = 0
for row in grid:
    #print("".join([str(v) for v in row]))
    for val in row:
        if val >= 2:
            count += 1

print("points with overlap >= 2: {}".format(count))
