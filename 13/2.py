import sys
data = open('input.txt').read().split('\n\n')
# data = open(sys.argv[1]).read().split('\n\n')
data = [x.split('\n') for x in data]
# look for horizontal and vertical mirrors
all_mirrors = []
for grid in data:
    mirror_found = False
    mirrors = []
    for i in range(len(grid[:-1])):
        smudges = 0
        reflection_len = min(i+1, len(grid)-i-1)
        for j in range(0, reflection_len):
            up = grid[i-j]
            down = grid[i+1+j]
            for idx in range(len(up)):
                if up[idx] != down[idx]:
                    smudges += 1
        if smudges == 1:
            mirrors.append((i+1)*100)
            break
    for i in range(0, len(grid[0])-1):
        smudges = 0
        reflection_len = min(i+1, len(grid[0])-1-i)
        for j in range(0,reflection_len):
            col_m1 = [row[i-j] for row in grid]
            col_m2 = [row[i+1+j] for row in grid]
            for idx in range(len(col_m1)):
                if col_m1[idx] != col_m2[idx]:
                    smudges += 1
        if smudges == 1:
            mirrors.append(i+1)   
            break 
    all_mirrors.append(mirrors)
all_sum = [b for a in all_mirrors for b in a]
print(sum(all_sum))

# too low 22528
# too low 25293