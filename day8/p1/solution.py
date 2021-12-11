# Read the input file
lines = []
with open('input.txt') as f:
    for line in f.readlines():
        line = line.strip('\n')
        lines.append(line)

def gen_lookup(patterns):
    # Segment count by digit:
    # 0: 6, abc efg
    # 1: 2,   c  f 
    # 2: 5, a cde g
    # 3: 5, a cd fg
    # 4: 4,  bcd f
    # 5: 5, ab d fg
    # 6: 6, ab defg
    # 7: 3, a c  f 
    # 8: 7, abcdefg
    # 9: 6, abcd fg

    # Assumption: we see examples of all 10 digits

    # Several digits are the only pattern
    # with a specific number of segments lit
    one = [p for p in patterns if len(p) == 2][0]
    seven = [p for p in patterns if len(p) == 3][0]
    four = [p for p in patterns if len(p) == 4][0]
    eight = [p for p in patterns if len(p) == 7][0]

    # In other cases, multiple digits
    # have the same number of segments lit
    two_three_five = [p for p in patterns if len(p) == 5]
    zero_six_nine = [p for p in patterns if len(p) == 6]

    # The difference between 1=cf and 7=acf is "a":
    a = seven - one

    # Now we know "a" for sure and c/f but not which is which.
    cf = one.intersection(seven)

    # The varying segments between 0, 6, and 9...
    # should be c, d, and e
    cde = zero_six_nine[0].symmetric_difference(zero_six_nine[1]).union(
            zero_six_nine[0].symmetric_difference(zero_six_nine[2]))

    c = cf.intersection(cde)
    de = cde - c
    f = cf - c

    # The varying segments between 2, 3, and 5...
    # should be b, c, e, f
    bcef = two_three_five[0].symmetric_difference(two_three_five[1]).union(
            two_three_five[0].symmetric_difference(two_three_five[2]))
    e = de.intersection(bcef)
    d = de - e
    b = bcef - cf - e
    g = eight - a - b - c - d - e - f

    # Now we should have a full mapping!
    print(a, b, c, d, e, f, g)

    zero = set().union(*[a, b, c, e, f, g])
    two = set().union(*[a, c, d, e, g])
    three = set().union(*[a, c, d, f, g])
    five = set().union(*[a, b, d, f, g])
    six = set().union(*[a, b, d, e, f, g])
    nine = set().union(*[a, b, c, d, f, g])

    lookup = {
        ''.join(sorted(zero)): 0,
        ''.join(sorted(one)): 1,
        ''.join(sorted(two)): 2,
        ''.join(sorted(three)): 3,
        ''.join(sorted(four)): 4,
        ''.join(sorted(five)): 5,
        ''.join(sorted(six)): 6,
        ''.join(sorted(seven)): 7,
        ''.join(sorted(eight)): 8,
        ''.join(sorted(nine)): 9,
    }
    return lookup

def str2set(s):
    return {c for c in s}

count = 0
for line in lines:
    patterns, values = line.split('|')
    patterns = [str2set(p) for p in patterns.split()]
    values = [''.join(sorted(s)) for s in values.split()]

    lookup = gen_lookup(patterns)
    for value in values:
        num = lookup[value]
        if num in {1, 4, 7, 8}:
            count += 1
print(count)

