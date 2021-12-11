# Read the input file
lines = []
with open('input.txt') as f:
    for line in f.readlines():
        line = line.strip('\n')
        lines.append(line)

def parse_line(line):
    return [int(c) for c in line.split(',')]

nums = parse_line(lines[0])

def compute_fuel(nums, pos):
    fuel = 0
    for num in nums:
        fuel += abs(num - pos)
    return fuel

# Let's be lazy and test all possibilities
min_pos = None
min_fuel = None
for pos in range(min(nums), max(nums) + 1):
    fuel = compute_fuel(nums, pos)
    print("position {} requires {} fuel".format(pos, fuel))
    if min_fuel is None or fuel < min_fuel:
        print("new minimum!")
        min_pos = pos
        min_fuel = fuel
print("min pos = {}, min fuel = {}".format(min_pos, min_fuel))