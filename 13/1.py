import sys
# data = open('input.txt').read().split('\n\n')
data = open(sys.argv[1]).read().split('\n\n')
data = [x.split('\n') for x in data]
# look for horizontal and vertical mirrors
all_mirrors = []
for grid in data:
    mirror_found = False
    mirrors = []
    for i in range(len(grid[:-1])):
        row2 = grid[i+1]
        row = grid[i]
        if row == row2:
            mirror_found = True
            reflection_len = min(i+1, len(grid)-i-1)
            for j in range(1, reflection_len):
                if grid[i-j] != grid[i+1+j]:
                    mirror_found = False
                    break
            if mirror_found:
                mirrors.append((i+1)*100)
                break
    for i in range(0, len(grid[0])-1):
        col1 = [row[i] for row in grid]
        col2 = [row[i+1] for row in grid]
        if col1 == col2:
            mirror_found = True
            reflection_len = min(i+1, len(grid[0])-1-i)
            for j in range(1,reflection_len):
                col_m1 = [row[i-j] for row in grid]
                col_m2 = [row[i+1+j] for row in grid]
                if col_m1 != col_m2:
                    mirror_found = False
                    break
            if mirror_found:
                mirrors.append(i+1)   
                break 
    all_mirrors.append(mirrors)
all_sum = [b for a in all_mirrors for b in a]
print(sum(all_sum))

# too low 22528
# too low 25293