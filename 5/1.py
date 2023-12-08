from dataclasses import dataclass
from typing import List

@dataclass
class My_Map:
    target: int
    source: int    
    range: int


def get_maps_from_input(lines: list) -> List[List[My_Map]]:
    maps_process = ''.join(lines[1:]).split('\n\n')
    maps_process = [m.split(':')[1] for m in maps_process]
    maps_process = [m.strip().split('\n') for m in maps_process]
    maps = []
    for ranges in maps_process:
        cur_map = []
        for r in ranges:
            int_vals = list(map(int,r.split()))
            cur_map.append(My_Map(*int_vals))
        maps.append(cur_map)
    return maps

# first - create maps from input

with open('input2.txt') as f:
    lines = f.readlines()

seeds = list(map(int,lines[0].split(':')[1].split()))
maps = get_maps_from_input(lines)
cur_min = seeds[0]
for seed in seeds:
    cur_val = seed
    for map in maps:
        for m in map:
            if m.source <= cur_val <= m.source + m.range:
                cur_val = m.target + cur_val - m.source
                break
    cur_min = min(cur_val, cur_min)
print(cur_min)
