import sys

f_name = sys.argv[1]
inp_ = open(f_name).read().strip().split('\n')
lines, instructions = [], []
for inp in inp_:
    line, instr = inp.split()
    instr = list(map(int,instr.split(',')))
    lines.append(list(line))
    instructions.append(instr)

def part1(line, ins):
    if '?' not in line:
        # if is_valid(line, ins):
        #     print(line, ins)
        return is_valid(line, ins)
    solution = 0
    i = line.index('?')
    line[i] = '#'
    solution += part1(line, ins)
    line[i] = '.'
    solution += part1(line, ins)
    line[i] = '?'  # Reset the change for the next iteration
    return solution

def is_valid(line, instr):
    cur = 0
    ins = 0
    for i in line:
        if i != '#' and i != '.':
            return False
        if i == '#':
            cur +=1
            continue
        if i == '.' and cur:
            if ins >= len(instr) or instr[ins] != cur:
                return False
            ins += 1
            cur = 0
    if cur:
        if ins >= len(instr) or instr[ins] != cur:
            return False
        ins +=1
    return ins == len(instr)

output = 0
for line, ins in zip(lines, instructions):
    print(line, ins)
    cur = part1(line, ins)
    print(cur)
    output += cur

print(output)