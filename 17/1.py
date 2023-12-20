from typing import List, Dict, Tuple
import heapq

file_path: str = 'input2.txt'
data_str: List[str] = open(file_path).read().strip().split('\n')
data: List[List[int]] = [[int(a) for a in row] for row in data_str]
directions: Dict[str, Tuple[int, int]] = {
    'N': (-1, 0),
    'W': (0, -1),
    'E': (0, 1),
    'S': (1, 0),
}

def get_neighbors(grid: List[List[int]], node: Tuple[int, int], prev_dir: Tuple[str, int]) -> List[Tuple[Tuple[int, int], Tuple[str, int]]]:
    neighbors = []
    for n,d in directions.items():
        new_node: Tuple[int,int] = (node[0]+ d[0], node[1] + d[1])
        # here i maybe should make sure that we are not going back but it is always going to be more expensive so not really
        if 0 <= new_node[0] < len(grid) and 0 <= new_node[1] < len(grid[new_node[0]]):
            if prev_dir[1] < 5 or prev_dir[0] != n:
                cur_dir = (n, 1 if prev_dir != n else prev_dir[1]+1)
                neighbors.append((new_node, cur_dir))
    return neighbors

def dijkstra(grid: List[List[int]], destination: Tuple[int,int]):
    weights: List[List[float]] = [[float('inf') for _ in row] for row in data]
    start = (0,0)
    weights[start[0]][start[1]] = grid[start[0]][start[1]]
    q: List[Tuple[int, Tuple[int, int], Tuple[str, int] ]] = []
    heapq.heappush(q, (grid[start[0]][start[1]], start, ('S', 3)))
    while q:
        cur_wieght, current_node, prev_dir = heapq.heappop(q)
        # print(current_node)
        if current_node == destination:
            return cur_wieght, weights
        neigh = get_neighbors(grid, current_node, prev_dir)
        for n, cur_dir in neigh:
            if cur_wieght + grid[n[0]][n[1]] < weights[n[0]][n[1]]:
                weights[n[0]][n[1]] = cur_wieght + grid[n[0]][n[1]]
                heapq.heappush(q, (weights[n[0]][n[1]], n,cur_dir))
    return 'not_found', weights

dest = (len(data)-1, len(data[len(data)-1])-1)
# dest = (2,6)
print(dest)
print(len(data))
output, weights = dijkstra(data, dest)
with open('wieghts.txt', 'w') as f:
    for row in weights:
        for i in row:
            f.write(str(i)+ '\t')
        
        f.write('\n')
print(output)




