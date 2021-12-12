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

def find_all_paths(connections, prefix):
    paths = []
    for dst in connections[prefix[-1]]:
        if dst == 'end':
            paths.append(prefix + ['end'])
        elif dst == dst.lower() and dst in prefix:
            print('cannot revisit dst {}'.format(dst))
            continue
        else:
            print('prefix {} can connect to dst {}...'.format(prefix, dst))
            new_paths = find_all_paths(connections, prefix + [dst])
            print('found {} new paths through dst {}'.format(len(new_paths), dst))
            paths.extend(new_paths)
    return paths

all_paths = find_all_paths(connections, ['start'])
print('found {} paths'.format(len(all_paths)))