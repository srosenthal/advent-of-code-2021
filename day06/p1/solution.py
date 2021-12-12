reset_age = 6
new_age = 8
num_days = 80

# Read the input file
lines = []
with open('input.txt') as f:
    for line in f.readlines():
        line = line.strip('\n')
        lines.append(line)

state = [int(n) for n in lines[0].split(',')]

def state2str(state):
    return ','.join([str(n) for n in state])

def update_state(old_state):
    new_state = []
    births = 0
    for s in old_state:
        if s == 0:
            births += 1
            new_state.append(reset_age)
        else:
            new_state.append(s - 1)
    new_state.extend([new_age] * births)
    return new_state

print('Initial state: {}'.format(state2str(state)))
for day in range(1, num_days + 1):
    state = update_state(state)
    #print('After\t{} days: {}'.format(day, state2str(state)))

print('Total fish = {}'.format(len(state)))
