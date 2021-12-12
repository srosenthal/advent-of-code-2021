# Read the input file
lines = []
with open('input.txt') as f:
    for line in f.readlines():
        line = line.strip('\n')
        lines.append(line)

pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
def compute_score(line):
    stack = []
    for c in line:
        if c in pairs.keys():
            # it's always valid to open parens
            stack.append(c)
        else:
            # closing: must match the most recently opened parens
            prev = stack.pop()
            expected = pairs[prev]
            if c != expected:
                print('Expected {}, but found {} instead'.format(expected, c))
                return scores[c]
    # Line is valid or simply incomplete.
    # We don't distinguish between those cases yet.
    return 0

total = 0
for line in lines:
    total += compute_score(line)
print(total)
