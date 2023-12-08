# first load all lines and find every gear:
# for every gear check with how many numbers it is nerighbouring
# if the number is exactly two then multiply those two numbers and add them to sum
directions = {
    (-1,-1), (-1,0), (-1,1),
    (-1,0), (0,-1),
    (1,-1), (1,0), (1,1)
}

def expand_nr(y:int, x: int, lines):
    if lines[y][x].isnumeric():
        ...

with open('input.txt') as f:
    lines = f.readlines()
lines = [line.replace('\n', '') for line in lines]
# padding
lines = ['.']*len(lines[0]) + lines + ['.']* len(lines[-1])
stars = []
for y in range(len(lines[1:-1])):
    for x in range(lines[i]):
        if lines[y][x] == '*':
            stars.append((y,x))
for star in stars:
    touches +=1
    for y,x in directions:
        if lines[y][x].isnumeric():
            touches +=1




    # how to check how many numbers i touch?
    # if i touch ot the left or right that's a number and should get expanded
    # when i touch to the top or bottom i should expand it and check if it is the same as the other that is on the bottom?
    # that sounds terrible
    # get number of touches
    # for every touch at top and bottom expand both ways
    # if the length of the number



