# go trough a line and when i find a numeral i check around this number and if i find i toggle the check flag
# if i don't find it i go to the next character if it is numeral i check again
# if i never find i don't do anything
# if i find a noncharacter or the end of the line after the numeral and check is toggled i add it to sum
# too high
from typing import List, Tuple
directions = [
    (1,1), (1,0), (1,-1),
    (0, -1), (0,1),
    (-1, 1), (-1,0), (-1,-1)
]

def check_around(cords: Tuple[str, str], table:List[str])-> bool:
    for dirs in directions:
        dy = dirs[0]
        dx = dirs[1]
        if cords[0]+dy < 0 or cords[1]+dx < 0 or cords[0]+dy >= len(table) or cords[1]+dx >= len(table[cords[1]]):
            continue ## oob check
        else:
            search = table[cords[0]+dy ][cords[1]+dx]
            if not search.isdigit() and not search == '.' :
                return True
    return False

sum = 0
previous = ''
cur_num = 0
check = False
with open('input.txt') as f:
    # striping from \n
    all_lines = [line[:-1] for line in f.readlines()]

for line_nr in range(len(all_lines)):
    line = all_lines[line_nr]
    for ind in range(len(line)):
        c = line[ind]
        if c.isdigit():
            if not check:
                check = check_around((line_nr, ind), all_lines)
            cur_num = cur_num*10 + int(c)
        else:
            if cur_num and check:              
                sum+=cur_num
            cur_num = 0
            check = False
    if cur_num and check:     
        sum+=cur_num
    cur_num = 0
    check = False
print(sum)
        # here maybe we need to add the number at the end of a line


        
    



