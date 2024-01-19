# going from top left and to the right
# on every grid point mark as energized
# how can in know if there are infinite loops in the grid?
# checking for infinite loop can be done by checking if in this grid point i have already went in the same direction before
# keep track of the current beam in a queue or a list because of splitting?
# %%
import sys
from typing import Tuple, List, Dict
grid = open(sys.argv[1]).read().strip().split('\n')
visited = [[False]*len(grid[0]) for _ in grid]
loop_check: List[List[List[str]]] = [[[] for _ in row] for row in grid]
directions: Dict[str, Tuple[int, int]] = {
    'N': (-1, 0),
    'S': (1, 0),
    'W': (0, -1), 
    'E': (0, 1)
}

back_slash = {
    'S': 'E',
    'E': 'S', 
    'N': 'W',
    'W': 'N'
}
forward_slash = {
    'S': 'W',
    'W': 'S', 
    'N': 'E',
    'E': 'N'
}


def part1(start: Tuple[Tuple[int, int], str], grid):
    visited = [[False]*len(grid[0]) for _ in grid]
    loop_check: List[List[List[str]]] = [[[] for _ in row] for row in grid]
    q: List[Tuple[Tuple[int, int], str]] = []
    q.append(start)
    while q:
        (y, x), direction = q.pop()
        
        if not (len(grid) > y >= 0) or not (len(grid[y]) > x >= 0):
            continue
        cur_point = grid[y][x]
        # print((y, x), direction, cur_point)
        if visited[y][x]:
            if direction in loop_check[y][x]:
                continue
        else:
            visited[y][x] = True
            loop_check[y][x].append(direction)
        if cur_point == '.':
            new_dir = direction
        elif cur_point == '/':
            new_dir = forward_slash[direction]
        elif cur_point == '\\':
            new_dir = back_slash[direction]
        elif cur_point == '|':
            if (direction == 'E' or direction == 'W'):
                dy, dx = directions['S']
                new_point = (y+dy, x + dx)
                q.append((new_point, 'S'))
                dy, dx = directions['N']
                new_point = (y+dy, x + dx)
                q.append((new_point, 'N'))
                continue
            else:
                new_dir = direction
        elif cur_point == '-':
            if (direction == 'S' or direction == 'N'):
                dy, dx = directions['E']
                new_point = (y+dy, x + dx)
                q.append((new_point, 'E'))
                dy, dx = directions['W']
                new_point = (y+dy, x + dx)
                q.append((new_point, 'W'))
                continue
            else:
                new_dir = direction
        dy, dx = directions[new_dir]
        new_point = (y+dy, x + dx)
        q.append((new_point, new_dir))
    
    return sum([sum(row) for row in visited])

# %%
# part2
top_row = [((0, x), 'S') for x in range(len(grid[0]))]
bot_row = [((len(grid)-1, x), 'N') for x in range(len(grid[0]))]
right_col = [((y, len(grid[0])-1), 'W') for y in range(len(grid))]
left_col = [((y, 0), 'E') for y in range(len(grid))]
starts = top_row + bot_row + right_col + left_col
maxx = 0
print(starts)
for start in starts:
    cur = part1(start, grid)
    maxx = max(maxx, cur)
    print(start, cur)
print(maxx)
         
output = part1(((0,0), 'E'), grid)
print(output)