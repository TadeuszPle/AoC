with open('input.txt') as f:
    lines = f.readlines()
instructions,_, *mappings = lines
instructions = instructions.strip()
keys = [line.strip().split('=')[0].strip() for line in mappings]
values = []
for line in mappings:
    directions = line.strip().split('=')[1]
    directions = directions.replace(')', '').replace('(','').replace(',','').split()
    values.append(tuple(directions))

d = dict(zip(keys, values))

cur_pos = keys[0]
steps = 0
nr_inst = len(instructions)
while cur_pos != keys[-1]:
    inst_ind = steps % nr_inst
    cur_inst = instructions[inst_ind]
    cur_pos = d[cur_pos][0] if cur_inst == 'L' else d[cur_pos][1] 
    steps += 1
print(steps)
