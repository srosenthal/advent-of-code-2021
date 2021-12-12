with open('input.txt') as f:
    sums = None
    count = 0
    for line in f.readlines():
        line = line.strip('\n')
        N = len(line)
        if sums is None:
            sums = [0] * N
        for i in range(0, N):
            c = line[i]
            if c == '1':
                sums[i] += 1
        count += 1

avgs = [s * 1.0 / count for s in sums]
print("sums = {}, count = {}, avgs = {}".format(sums, count, avgs))

# each bit of gamma is the most common bit
# episilon has the opposite bits
gamma_bits = ''.join(['1' if s > count / 2 else '0' for s in sums])
eps_bits = ''.join(['1' if c == '0' else '0' for c in gamma_bits])

gamma = int(gamma_bits, 2)
eps = int(eps_bits, 2)
print("gamma = {}, eps = {}, product = {}".format(gamma, eps, gamma * eps))
