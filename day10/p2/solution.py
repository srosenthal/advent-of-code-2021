# Read the input file
lines = []
with open('input.txt') as f:
    for line in f.readlines():
        line = line.strip('\n')
        lines.append(line)

pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
scores = {')': 1, ']': 2, '}': 3, '>': 4}
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
                return 0
    if len(stack) > 0:
        closers = list(reversed([pairs[c] for c in stack]))

        total = 0
        for closer in closers:
            total = total * 5 + scores[closer]
        
        print('Incomplete line, completed by {} -> {} points'.format(''.join(closers), total))

        return total

    print('Complete line')
    return 0

all_scores = []
for line in lines:
    print('Processing line: {}'.format(line))
    score = compute_score(line)
    if score > 0:
        all_scores.append(score)

from statistics import median
print(median(all_scores))
