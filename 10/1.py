import sys
from typing import Tuple, List, Dict, Optional

def get_start_pos(data: List[str]) -> Tuple[int, int]:
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[y][x] == 'S':
                return (y,x)
    raise ValueError("No start position found")

pipes : Dict[str, Tuple[int, int]] = {
    '|': (1, 0),
    '-': (0, 1),
    'L': (1, 1),
    '7': (1, 1), 
    'J': (1, -1),
    'F': (1, -1),
}
dirs: Dict[str, Tuple[int, int]] = {
    'S': (1, 0),
    'N': (-1, 0),
    'E': (0, 1),
    'W': (0, -1),
}
data: List[str] = open(sys.argv[1]).readlines()
start_pos = get_start_pos(data)
distances = [[float('inf')]*len(line) for line in data]
distances[start_pos[0]][start_pos[1]] = 0

def are_connected(start: Tuple[int, int], dest: Tuple[int, int], data: List[str]) -> bool:
    diff = (dest[0] - start[0], dest[1] - start[1])


def find_farthest(data: List[str], start_pos: Tuple[int, int], distances: List[List[]]) -> Optional[int]:
    pos = start_pos
    steps = 0
    while True:
        steps += 1
        for d in dirs:
            ...