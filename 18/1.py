input_file = 'input2.txt'
raw_lines = open(input_file).read().strip().split('\n')
instructions = [(line.split()[0], int(line.split()[1]), line.split()[2][1:-1]) for line in raw_lines]
directions = {
    'U':(-1,0),
    'D':(1,0),
    'L':(0,-1),
    'R':(0,1),
}
def get_grid_size(instrs):
    cur_pos = (0,0)
    max_h, min_h, max_w, min_w = 0,0,0,0
    for let,le,col in instrs:
        cur_dir = directions[let]
        d = (cur_dir[0]*le, cur_dir[1]*le)
        cur_pos = (cur_pos[0]+ d[0], cur_pos[1] + d[1])
        max_h = max(max_h, cur_pos[0])
        min_h = min(min_h, cur_pos[0])
        max_w = max(max_w, cur_pos[1])
        min_w = min(min_w, cur_pos[1])
    return min_h, min_w, max_h, max_w

def get_area(grid):
    area = 0
    for line in grid:
        print(area)
        last_one = None
        for i, c in enumerate(line):
            if c == 1:
                if last_one is not None:
                    area += i-last_one+1
                    last_one = None
                    
                else:
                    last_one = i
        if last_one:
            area += 1
    return area

min_h, min_w, max_h, max_w = get_grid_size(instructions)
width = max_w - min_w + 1
height = max_h - min_h + 1
print(width, height)
grid = [[0]*width for _ in range(height)]
start_pos = (-min_h, -min_w)
cur_pos = start_pos
grid[start_pos[0]][start_pos[1]] = 2
for ins_ind, (letter, le, col) in enumerate(instructions):
    
    cur_dir = directions[letter]
    y,x = cur_pos
    d = (cur_dir[0]*le, cur_dir[1]*le)
    print(ins_ind+1, y,x,d)
    if letter == 'D' or letter == 'U':
        for i in range(1,le+1):
            grid[y+i*cur_dir[0]][x] = 1
    else:
        for i in range(1,le+1):
            grid[y][x+i*cur_dir[1]] = 1
    
    cur_pos = y + d[0], x + d[1]
print(get_area(grid=grid))
with open('grid.txt', 'w') as f:
    for line in grid:
        for i in line:
            f.write(str(i))
        f.write('\n')  


        