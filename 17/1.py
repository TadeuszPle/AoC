from typing import List, Dict, Tuple
import queue

file_path: str = 'input2.txt'
data_str: List[str] = open(file_path).read().strip().split('\n')
data: List[List[int]] = [[int(a) for a in row] for row in data_str]
directions: Dict[str, Tuple[int, int]] = {
    'N': (-1, 0),
    'W': (0, -1),
    'E': (0, 1),
    'S': (1, 0),
}
# when I reach a certain point and there is no possible faster way to get there
# then I should mark it somehow?
# whenever I reach it
# mark all grids with infs
# go through my path and if my path is cheaper mark this place with this cheaper value
# make a constraint for 3 moves in one direction:
# after third move in the same direction give only two possibilities for the next step
weights: List[List[float]] = [[float('inf') for r in row] for row in data]

def dijkstra(grid: List[List[int]], destination: Tuple[int,int]):
    start = (0,0)
    q: queue.Queue[Tuple[int, int]] = queue.Queue()
    q.put(start)
    while q:
        current_node = q.get()
        prev_dir: Tuple[str, int] = ('Q', 0)




