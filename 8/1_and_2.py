import sys
import math
f_name = 'input.txt'
f_name = sys.argv[1]
with open(f_name) as f:
    lines = f.readlines()
instructions,_, *mappings = lines
instructions = instructions.strip()

d = {}
first = mappings[0].strip().split('=')[0][:-1]
for line in mappings:
    key, ds = line.strip().split('=')
    directions = [d.strip() for d in ds[2:-1].split(',')]
    d[key[:-1]] = directions
cur_pos = 'AAA'
steps = 0
nr_inst = len(instructions)
print(instructions)
while cur_pos != 'ZZZ':
    inst_ind = steps % nr_inst
    cur_inst = instructions[inst_ind]
    cur_pos = d[cur_pos][0] if cur_inst == 'L' else d[cur_pos][1] 
    steps += 1
print('part 1: ', steps)

starts = [k for k in d if k.endswith('A')]
mins = []
for start in starts:
    min_to_z = 0
    cur_pos = start
    while not cur_pos.endswith('Z'):
        instruction = instructions[min_to_z % len(instructions)]
        cur_pos = d[cur_pos][0] if instruction == 'L' else d[cur_pos][1]
        min_to_z += 1
    mins.append(min_to_z)
print(starts)
print(mins)
output = 1
for m in mins:
    output = math.lcm(output, m)
print(output)
