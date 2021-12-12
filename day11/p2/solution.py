# Read the input file
lines = []
with open('input.txt') as f:
    for line in f.readlines():
        line = line.strip('\n')
        lines.append(line)

def parse_line(line):
    return [int(c) for c in line]

def parse_lines(lines):
    state = []
    for line in lines:
        state.append(parse_line(line))
    return state

def row2str(row):
    return ''.join([str(n) for n in row])

def state2str(state):
    return '\n'.join([row2str(r) for r in state])

state = parse_lines(lines)
num_rows = len(state)
num_cols = len(state[0])

def list_neighbors(point):
    i, j = point
    output = []
    # up/down
    if i > 0:
        output.append((i - 1, j))
    if i < num_rows - 1:
        output.append((i + 1, j))
    # left/right
    if j > 0:
        output.append((i, j - 1))
    if j < num_cols - 1:
        output.append((i, j + 1))
    # diagonals also
    if i > 0 and j > 0:
        output.append((i - 1, j - 1))
    if i > 0 and j < num_cols - 1:
        output.append((i - 1, j + 1))
    if i < num_rows - 1 and j > 0:
        output.append((i + 1, j - 1))
    if i < num_rows - 1 and j < num_cols - 1:
        output.append((i + 1, j + 1))
    return output

def advance_step(state):
    print("advancing state by one step...")
    output = [row.copy() for row in state]

    to_flash = []  # (i, j) coords
    flashed = set()  # (i, j) coords
    
    # First, all values increase by one
    for i in range(num_rows):
        for j in range(num_cols):
            output[i][j] += 1
            if output[i][j] > 9:
                print("first pass: (i, j) = {} should flash".format((i, j)))
                flashed.add((i, j))
                to_flash.append((i, j))

    # Then any value > 9 flashes
    while len(to_flash) > 0:
        center = to_flash.pop(0)
        ci, cj = center
        neighbors = list_neighbors(center)
        for (i, j) in neighbors:
            print("considering neighbor {} of center {}".format((i, j), center))
            output[i][j] += 1
            if output[i][j] > 9 and (i, j) not in flashed:
                print("second pass: (i, j) = {} should also flash".format((i, j)))
                flashed.add((i, j))
                to_flash.append((i, j))

    # Then any coordinate that flashed resets to 0
    for (i, j) in flashed:
        print("third pass: (i, j) = {} resets to 0".format((i, j)))
        output[i][j] = 0

    all_flashed = len(flashed) == num_rows * num_cols

    return output, all_flashed

print('Before any steps:\n{}'.format(state2str(state)))

i = 1
while True:
    state, all_flashed = advance_step(state)
    print('\nAfter step {}:\n{}'.format(i, state2str(state)))
    if all_flashed:
        print('ALL flashed at step {}'.format(i))
        break;
    i += 1
