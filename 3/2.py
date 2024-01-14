# first load all lines and find every gear:
# for every gear check with how many numbers it is next to it
# if the number is exactly two then multiply those two numbers and add them to sum
import sys
directions = [
    (-1,-1), (-1,0), (-1,1),
    (0,-1), (0,1),
    (1,-1), (1,0), (1,1)
]
def get_touching_nrs(grid, yx):
    y, x = yx
    nrs = []
    for dy,dx in directions:
        nr = -1
        if grid[y+dy][x+dx].isnumeric():
            nr = expand_nr(y+dy, x+dx, grid)
        nrs.append(nr)
    #print(nrs)
    nrs = simplifiy_nrs(nrs)
    return nrs

def simplifiy_nrs(nrs):
    outcome = nrs
    if nrs[0] == nrs[1]:
        outcome = outcome[1:]
    if nrs[2] == nrs[1]:
        outcome = [outcome[0]] + outcome[2:]
    if nrs[-1] == nrs[-2]:
        outcome = outcome[:-1]
    if nrs[-3] == nrs[-2]:
        outcome = outcome[:-2] + [outcome[-1]]
    return [i for i in outcome if i > -1]


def expand_nr(y:int, x: int, grid):
    start, stop = x, x
    for i in range(x-1, -1, -1):
        if grid[y][i].isnumeric():
            start = i
        else:
            break

    for i in range(x+1, len(grid[y])):
        if grid[y][i].isnumeric():
            stop = i
        else:
            break   
    return int(grid[y][start:stop+1])
file_name = sys.argv[1]
with open(file_name) as f:
    lines = f.readlines()
lines = [line.replace('\n', '') for line in lines]
# padding
lines = ['.' + line + '.' for line in lines]
lines = ['.'*len(lines[0])] + lines +['.'*len(lines[-1])]

for line in lines:
    print(line)
stars = []
for y in range(len(lines[1:-1])):
    for x in range(len(lines[y])):
        if lines[y][x] == '*':
            stars.append((y,x))
output = 0
for y_s, x_s in stars:
    nrs = get_touching_nrs(lines, (y_s, x_s))
    print(nrs)
    if len(nrs) == 2:
        output += nrs[0]*nrs[1]
print(output)
        
# 30385280 too low
# 75275088 too low



    # how to check how many numbers i touch?
    # if i touch ot the left or right that's a number and should get expanded
    # when i touch to the top or bottom i should expand it and check if it is the same as the other that is on the bottom?
    # that sounds terrible
    # get number of touches
    # for every touch at top and bottom expand both ways
    # if the length of the number



