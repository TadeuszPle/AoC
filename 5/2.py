
from dataclasses import dataclass
from typing import List

@dataclass
class My_Range:
    target: int
    start: int    
    length: int
    end: int = None
    
    def __post_init__(self):
        self.end = self.start + self.length
    
    def map(self, value: int) -> int:
        if self.end > value >= self.start:
            return value - self.start + self.target
        else:
            return value


def get_maps_from_input(lines: list) -> List[List[My_Range]]:
    maps_process = ''.join(lines[1:]).split('\n\n')
    maps_process = [m.split(':')[1] for m in maps_process]
    maps_process = [m.strip().split('\n') for m in maps_process]
    maps = []
    for ranges in maps_process:
        cur_map = []
        for r in ranges:
            int_vals = list(map(int,r.split()))
            cur_map.append(My_Range(*int_vals))
        cur_map = sorted(cur_map, key=lambda x: x.start)  # Fix: Sort by 'start' attribute
        maps.append(cur_map)
    return maps

# first - create maps from input

with open('input2.txt') as f:
    lines = f.readlines()

seeds = map(int,lines[0].split(':')[1].split())
seeds = zip(seeds,seeds)
seeds = [(s[0], s[0]+s[1]) for s in seeds]
seeds.sort()  
maps = get_maps_from_input(lines)

next_map_input = []
for map in maps[:2]:
    
    cur_map_input = next_map_input if next_map_input else seeds
    print('---next map---')
    print(cur_map_input)

    next_map_input = []
    i = 0
    while i < len(cur_map_input):
        # curmap zamiast listy do deque? Ja pierdole
        start, end = cur_map_input[i]
        for range in map:
            # retadred solve:
            # divide into 6 posibilities:
            # 1 and 6 -> outside of range
            # 2 partial overlap from right
            # 3 complete overlap
            # 4 complete overflow
            # 5 partial overlap from left
            # 1 and 6
            no_overlap = None
            if (start > range.end):
                # this and every next seed is too high for this range
                next_map_input.append((start, end))
                break
            if (end < range.start):
                next_map_input.append((start, end))
                continue        
            # 2
            if start < range.start and range.start < end <= range.end:
                overlap = (range.start, end)
                next_map_input.append((start, range.start))
            # 3
            if start >= range.start and end <= range.end:
                overlap = (start, end)
                no_overlap = None
            # 4 
            if start < range.start and end > range.end:
                overlap = (range.start, range.end)
                next_map_input.append((start, range.start))
                no_overlap =  (range.end, end)
            # 5 
            if range.start <= start < range.end and end > range.end:
                overlap = (start, range.end)
                no_overlap = (range.end, end)
            print(f"{(start, end)}, {(range.start, range.end)} ")
            print(f"overlap: {overlap}")
            print(f"no overlap {no_overlap}")
            next_map_input.append(overlap)
            # no overlap could be appended after calculation tbh
            if no_overlap:
                cur_map_input.append(no_overlap)
        i+=1
    next_map_input.sort()
    print(next_map_input)
print(next_map_input[0])


    
