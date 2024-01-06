import sys
from typing import Tuple, List, Dict, Optional

def get_start_pos(data: List[str]) -> Tuple[int, int]:
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[y][x] == 'S':
                return (y,x)
    raise ValueError("No start position found")

pipes : Dict[str, Tuple[str, str]] = {
    '.': ('X', 'X'),
    '|': ('S', 'N'),
    '-': ('E', 'W'),
    'L': ('N', 'W'),
    '7': ('S', 'E'), 
    'J': ('N', 'E'),
    'F': ('S', 'W'),
}
dirs: Dict[str, Tuple[int, int]] = {
    'S': (1, 0),
    'N': (-1, 0),
    'E': (0, 1),
    'W': (0, -1),
    'X': (0, 0),
}
data: List[str] = open(sys.argv[1]).read().strip().split('\n')
start_pos = get_start_pos(data)
distances = [[float('inf')]*len(line) for line in data]
distances[start_pos[0]][start_pos[1]] = 0

# def are_connected(start: Tuple[int, int], dest: Tuple[int, int], data: List[str]) -> bool:
#     diff = (dest[0] - start[0], dest[1] - start[1])

def find_farthest(data: List[str], start_pos: Tuple[int, int], distances: List[List[float]]) -> Optional[int]:
    pos = start_pos
    x_p, y_p = start_pos
    q = []
    for d in dirs:
        new_pos = (y_p + dirs[d][0], x_p + dirs[d][1])
        new_pipe = data[new_pos[0]][new_pos[1]]
        pipe_dirs = pipes[new_pipe]
        if (new_pos[0] - y_p, new_pos[1] - x_p) == dirs[pipe_dirs[0]] or (new_pos[0] - y_p, new_pos[1] - x_p) == dirs[pipe_dirs[1]]:
            q.append((new_pos, pos))

    while q:
        (y1, x1), (y_p, x_p) = q.pop()
        cur_dist: float = distances[y_p][x_p] + 1
        if (y1, x1) == start_pos:
            continue
        if distances[y1][x1] <= cur_dist:
            return distances[y1][x1]
        distances[y1][x1] = cur_dist
        cur_pipe = data[y1][x1]
        cur_dirs = pipes[cur_pipe]
        next_dir_str = cur_dirs[0] if (y1-y_p, x1-x_p) == dirs[cur_dirs[1]]  else cur_dirs[1]
        next_dir = dirs[next_dir_str]
        next_pos = (y1+ next_dir[0], x1 + next_dir[1])
        q.append((next_pos, (y1, x1)))
    return None
far = find_farthest(data, start_pos, distances)
print(far)
# one approach is dumb -> look in every direction and see if it is connected to the current position
# another approach is to go in the directions that the actual pipes point to
# how can i do that?
# at the start i need to find the two connected pipes. They can be in any direction
# once i have found them, i can go in the direction that they point to
# but where i go is different when i am going from south and when i am going from north
            # in one situation the direction is exactly opposite 
            # maybe it is not opposite but different -> two cases
            # L i can go in two directions one of them i came from.
    # if i came from this direction then i pick the other one
    # simple as