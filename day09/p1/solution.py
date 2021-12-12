# Read the input file
lines = []
with open('input.txt') as f:
    for line in f.readlines():
        line = line.strip('\n')
        lines.append(line)

grid = []
for line in lines:
    grid.append([int(c) for c in line])

def compute_risk(height):
    return height + 1

total_risk = 0
num_rows = len(grid)
num_cols = len(grid[0])
for i in range(num_rows):
    for j in range(num_cols):
        is_low = (i == 0 or grid[i][j] < grid[i-1][j]) and \
                 (i == num_rows-1 or grid[i][j] < grid[i+1][j]) and \
                 (j == 0 or grid[i][j] < grid[i][j-1]) and \
                 (j == num_cols-1 or grid[i][j] < grid[i][j+1])
        if is_low:
            print("(i, j) = ({}, {}) is a low point".format(i, j))
            total_risk += compute_risk(grid[i][j])
print(total_risk)
        