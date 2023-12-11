import sys
from typing import List, Tuple
space:List[str] = open(sys.argv[1]).readlines()
space = [line.strip() for line in space]
print(len(space), len(space[0]))
empty_lines: List[int] = []
for i,line in enumerate(space):
    if '#' not in line:
        empty_lines.append(i)

empty_rows: List[int] = []
for i in range(len(space[0])):
    if '#' not in [line[i] for line in space]:
        empty_rows.append(i)


expand = int(1e6)
for part2 in [False, True]:
    galaxies_inds: List[Tuple[int,int]] = []
    for i in range(len(space)):
        for j in range(len(space[i])):
            if space[i][j] == '#':
                galaxies_inds.append((i,j))
    total_dist = 0
    while galaxies_inds:
        y1,x1 = galaxies_inds.pop()
        for y2, x2 in galaxies_inds:
            distance = abs(y1-y2) + abs(x1-x2)
            for er in empty_rows:
                if er in range(min(x1,x2)+1, max(x1,x2)):
                    expance = expand if part2 else 2
                    distance += expance-1
            for el in empty_lines:
                if el in range(min(y1,y2)+1, max(y1,y2)):
                    expance = expand if part2 else 2
                    distance += expance-1
            total_dist += distance
    print(total_dist)

# 483845200392 too high :<
