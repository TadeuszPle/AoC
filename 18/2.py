input_file = 'input2.txt'
raw_lines = open(input_file).read().strip().split('\n')
instructions = [(line.split()[0], int(line.split()[1]), line.split()[2][1:-1]) for line in raw_lines]
directions = {
    'U':(-1,0),
    'D':(1,0),
    'L':(0,-1),
    'R':(0,1),
}
hex_directions = {3:'U',    1:'D',    2:'L',    0:'R'}
vertices = []
for direction, _, hex_ in instructions:
    le = int(hex_[:-1],16)
    d = directions[hex_directions[hex_[-1]]]
    
    cur_pos = (cur_pos[0]+d[0]*, cur_pos[1] + d[1])
    vertices.append(cur_pos)