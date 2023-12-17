import sys
from typing import List, Tuple
file_path: str = 'input.txt'
grid: List[str] = open(file_path).read().strip().split('\n')
p1: int = 0
def calc_weight(nr_rocks: int, l_hash: int) -> int:
    rs = [len(column)-l_hash-b-1 for b in range(nr_rocks)]
    print(rs)
    return sum(rs)
for i in range(len(grid[0])):
    # go through a column and split by #
    # if there is with 'o's (mandatory) and dots (optional)
    # count the number of 'o's and add index+1 of the last # to the result
    column: str = ''.join([row[i] for row in grid])
    splits: List[str] = column.split('#')
    rocks: int = 0
    last_hash: int = -1

    for c_i in range(len(column)):
        c = column[c_i]
        if c == '#':
            if rocks:
                cur_weight = calc_weight(rocks, last_hash)
                p1 += cur_weight
                # (last_hash + last_hash + rocks-1)/2 * rocks/2
            rocks = 0
            last_hash = c_i
        if c == 'O':
            rocks += 1
    cur_weight = calc_weight(rocks, last_hash)
    p1 += cur_weight
print(p1)

# 1992 too low