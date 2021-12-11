reset_age = 6
new_age = 8
num_days = 256

# Read the input file
lines = []
with open('input.txt') as f:
    for line in f.readlines():
        line = line.strip('\n')
        lines.append(line)

starting_ages = [int(n) for n in lines[0].split(',')]

# 256 days runs slowly with the previous solution

# A closed form solution doesn't seem obvious.
# Ah! What if we bucket the fishes?
# To model the school of fish,
# we only ever need to know how many of each age.

# New state vector can be:
# [# of fish of age 0, # of fish of age 1, ...]

def empty_state():
    return [0] * (max(reset_age, new_age) + 1)

def state2str(state):
    return str(state)

def update_state(state):
    new_state = empty_state()
    num_spawning = state[0]

    # all fish get one day older
    new_state = state[1:] + [0]

    # spawning fish reset
    new_state[reset_age] += num_spawning
    new_state[new_age] += num_spawning

    return new_state

state = empty_state()
for age in starting_ages:
    state[age] += 1

print('Initial state: {}'.format(state2str(state)))
for day in range(1, num_days + 1):
    state = update_state(state)
    print('After\t{} days: {}'.format(day, state2str(state)))

print('Total fish = {}'.format(sum(state)))
