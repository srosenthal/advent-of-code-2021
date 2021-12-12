from collections import defaultdict

# Read the input file
lines = []
with open('input.txt') as f:
    for line in f.readlines():
        line = line.strip('\n')
        lines.append(line)

connections = defaultdict(set)
for line in lines:
    src, dst = line.split('-')
    connections[src].add(dst)
    connections[dst].add(src)

def can_visit(prefix, dst):
    if dst != dst.lower():
        # dst is large cave
        return True
    elif dst not in prefix:
        # can always visit a new cave
        return True
    else:
        # dst is small cave, and a repeat
        if dst == 'start':
            # can never repeat 'start'
            return False
        # we can visit only if we haven't repeated any small cave yet
        small = [cave for cave in prefix if cave.lower() == cave]
        return len(small) == len(set(small))

def find_all_paths(connections, prefix):
    paths = []
    for dst in connections[prefix[-1]]:
        if dst == 'end':
            paths.append(prefix + ['end'])
        elif can_visit(prefix, dst):
            print('prefix {} can connect to dst {}...'.format(prefix, dst))
            new_paths = find_all_paths(connections, prefix + [dst])
            print('found {} new paths through dst {}'.format(len(new_paths), dst))
            paths.extend(new_paths)
        else:
            print('cannot visit dst {}'.format(dst))
            continue

    return paths

all_paths = find_all_paths(connections, ['start'])
print('found {} paths'.format(len(all_paths)))