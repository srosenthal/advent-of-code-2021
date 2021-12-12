# life support rating = (oxygen generator rating) * (CO2 scrubber rating)
# filter based on "bit criteria" until only one number is remaining
#
# for oxygen generator rating:
# working left to right, keep the numbers with the most common bit value in the current position
# continue until only one number is left
#
# for CO2 scrubber rating:
# do the same but with least common bit values

# read the lines from the file
lines = []
with open('input.txt') as f:
    for line in f.readlines():
        line = line.strip('\n')
        lines.append(line)

def compute_averages(lines):
    sums = None
    count = 0
    for line in lines:
        N = len(line)
        if sums is None:
            sums = [0] * N
        for i in range(0, N):
            c = line[i]
            if c == '1':
                sums[i] += 1
        count += 1
    avgs = [s * 1.0 / count for s in sums]
    return avgs

i = 0
ox_lines = lines
while len(ox_lines) > 1:
    avgs = compute_averages(ox_lines)
    print('avgs = {}'.format(avgs))
    most_common = '1' if avgs[i] >= 0.5 else '0'
    ox_lines = [line for line in ox_lines if line[i] == most_common]
    print('oxygen generator rating: after position {}, len = {}'.format(i, len(ox_lines)))
    print('remaining options = {}'.format(ox_lines))
    i += 1
ox_bits = ox_lines[0]
ox_rating = int(ox_bits, 2)
print('oxygen bits = {}, rating = {}'.format(ox_bits, ox_rating))

i = 0
co2_lines = lines
while len(co2_lines) > 1:
    print('computing averages...')
    avgs = compute_averages(co2_lines)
    print('avgs = {}'.format(avgs))
    most_common = '1' if avgs[i] >= 0.5 else '0'
    co2_lines = [line for line in co2_lines if line[i] != most_common]
    print('co2 scrubber rating: after position {}, len = {}'.format(i, len(co2_lines)))
    print('remaining options = {}'.format(co2_lines))
    i += 1
co2_bits = co2_lines[0]
co2_rating = int(co2_bits, 2)
print('co2 bits = {}, rating = {}'.format(co2_bits, co2_rating))

print(ox_rating * co2_rating)

