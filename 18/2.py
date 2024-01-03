input_file = 'input.txt'
raw_lines = open(input_file).read().strip().split('\n')
instructions = [(line.split()[0], int(line.split()[1]), line.split()[2][1:-1]) for line in raw_lines]
directions = {
    'U':(-1,0),
    'D':(1,0),
    'L':(0,-1),
    'R':(0,1),
}
def calc_area(verts):
    sum = 0
    y,x = verts[0]
    for (y1, x1) in verts[1:-1]:
        sum += (y+y1) * (x-x1) 
        # sum += (y*x1)-(y1*x)
        y,x = y1, x1
    return abs(sum/2)

def picks(area, verts):
    # to the area we need to add every point that is in between the vertices -> it is on the grid just like the vertices
    x,y = (0,0)
    on_grid = 0
    for (y1,x1) in verts[1:]:
        on_grid +=  abs(x1-x + y1-y)
        x,y = x1,y1
    print('chuj' , on_grid)
    return int(area - on_grid/2 + 1) + on_grid


def solve(part2: bool):
    hex_directions = {3:'U',    1:'D',    2:'L',    0:'R'}
    vertices = []
    cur_pos = (0,0)
    for direction, le_part1, hex_ in instructions:
        le = int(hex_[1:-1],16) if part2 else le_part1
        d = directions[hex_directions[int(hex_[-1])]] if part2 else directions[direction]
        cur_pos = (cur_pos[0]+d[0]*le, cur_pos[1] + d[1]*le)
        vertices.append(cur_pos)
    area = picks(calc_area(vertices), vertices)

    print(area)
for a in [False, True]:
    solve(a)


# # really nice zniperr solution 
# import sys
# from itertools import accumulate, pairwise

# def parse(line):
#     direction, distance, color = line.split()
#     d = int(distance)
#     yield ((d, 0), (0, d), (-d, 0), (0, -d))['RDLU'.index(direction)]
#     d = int(color[2:7], 16)
#     yield ((d, 0), (0, d), (-d, 0), (0, -d))[int(color[7])]

# def dig(steps):
#     xy = list(zip(*map(accumulate, zip(*steps))))
#     return sum(xa * yb - ya * xb + abs(xb - xa + yb - ya)
#                for (xa, ya), (xb, yb) in pairwise(xy + xy[:1])) // 2 + 1

# wrong, color = zip(*map(parse, sys.stdin))
# print(dig(wrong))
# print(dig(color))