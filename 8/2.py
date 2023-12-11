from functools import reduce
from math import gcd
import sys

instructions,_, *mappings = open(sys.argv[1]).readlines()
instructions = instructions.strip()
keys = [line.strip().split('=')[0].strip() for line in mappings]
values = []
for line in mappings:
    directions = line.strip().split('=')[1]
    directions = directions.replace(')', '').replace('(','').replace(',','').split()
    values.append(tuple(directions))

d = dict(zip(keys, values))


cur_pos = [p for p in keys if p.endswith('A')]
cycles = []
for pos in cur_pos:
    step = 0
    first_z = None
    cycle = []
    while True:
        while step == 0 or not pos.endswith('Z'):
            step +=1
            cur_inst = instructions[step % len(instructions)]
            pos = d[pos][0 if cur_inst == 'L' else 1]
        
        cycle.append(step)
        step = 0
        # checking if i returned to the first Z position
        if first_z is None:
            first_z = pos
        elif pos == first_z:
            break
    cycles.append(cycle)
loops = [c[0] for c in cycles]
print(cur_pos)
print(loops)

reduce_gcd = reduce(lambda acum,y: acum*y//gcd(acum,y), loops, 1)
print(reduce_gcd)