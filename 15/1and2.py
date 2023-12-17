import sys
file_path = 'input.txt'
data = open(file_path).read().strip()
output = 0
parts = data.split(',')
parts_results = []
def hash_(s:str)->int:
    current = 0
    for c in s:
        current = ((current + ord(c))*17) % 256
    return current
part1 = 0
for part in parts:
    part1 += hash_(part)

# ----part2 ----
boxes = [[] for _ in range(256)]
for part in parts:
    idx = None
    focal_len = None
    for i in range(1, len(part)):
        if part[i] == '-':
            add = False
            idx = i
            break
        if part[i] == '=':
            add = True
            idx = i
            focal_len = int(part[idx + 1])
            break
    label = part[:idx]
    box_ind = hash_(label)
    ind_in_box = None
    for i in range(len(boxes[box_ind])):
        if boxes[box_ind][i][0] == label:
            ind_in_box = i
            break
    if add:
        if ind_in_box is not None:
            boxes[box_ind][ind_in_box] = (label, focal_len)
        else:
            boxes[box_ind].append((label, focal_len))
    else:
        if ind_in_box is not None:
            del boxes[box_ind][ind_in_box]
part2 = 0
for b_ind, box in enumerate(boxes):
    for i, lens in enumerate(box):
        #print((b_ind+1)*(i+1)*lens[1])
        part2 +=(b_ind+1)*(i+1)*lens[1]




# print(parts_results)
output = sum(parts_results)
print(part1)
print(part2)
# too low 511410