from functools import reduce
from operator import mul
total = 0
break_flag = False
with open('input.txt') as f:
    for line in f:
        min_for_color = {'red': 0 , 'blue': 0, 'green': 0}
        game_ind, game = line.split(':')
        game_splits = game.split(';')
        for split in game_splits:
            colors = split.split(',')
            for color in colors:
                nr, c = color.split()
                if int(nr) > min_for_color[c]:
                    min_for_color[c] = int(nr)

    
        total += reduce(mul,map(int,min_for_color.values()))
print(total)
        