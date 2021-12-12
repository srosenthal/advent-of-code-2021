# Read the input file
lines = []
with open('input.txt') as f:
    for line in f.readlines():
        line = line.strip('\n')
        lines.append(line)

grid = []
for line in lines:
    grid.append([int(c) for c in line])

num_rows = len(grid)
num_cols = len(grid[0])

# find low points
low_points = []
for i in range(num_rows):
    for j in range(num_cols):
        is_low = (i == 0 or grid[i][j] < grid[i-1][j]) and \
                 (i == num_rows-1 or grid[i][j] < grid[i+1][j]) and \
                 (j == 0 or grid[i][j] < grid[i][j-1]) and \
                 (j == num_cols-1 or grid[i][j] < grid[i][j+1])
        if is_low:
            print("(i, j) = ({}, {}) is a low point".format(i, j))
            low_points.append((i, j))

# for each low point, expand to its basin and compute area
# ... graph traversal

def list_neighbors(point):
    i, j = point
    output = []
    if i > 0:
        output.append((i - 1, j))
    if i < num_rows - 1:
        output.append((i + 1, j))
    if j > 0:
        output.append((i, j - 1))
    if j < num_cols - 1:
        output.append((i, j + 1))
    return output

def compute_basin_size(point):
    basin = {point}
    visited = set(point)
    queue = list_neighbors(point)
    while len(queue) > 0:
        neighbor = queue.pop()
        visited.add(neighbor)
        i, j = neighbor
        if grid[i][j] < 9:
            print("extending basin to point ({}, {})".format(i, j))
            basin.add(neighbor)
            rest = [p for p in list_neighbors(neighbor) if p not in visited]
            queue.extend(rest)
    size = len(basin)
    print("basin centered around ({}, {}) has size {}".format(point[0], point[1], size))
    return size

point_to_size = {}
for low_point in low_points:
    size = compute_basin_size(low_point)
    point_to_size[low_point] = size

# compute the product of the 3 largest basins
from math import prod
print(prod(list(reversed(sorted(point_to_size.values())))[0:3]))
