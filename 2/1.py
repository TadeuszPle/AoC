total = 0
break_flag = False
max_for_color = {'red': 12 , 'blue': 14, 'green': 13}
with open('input.txt') as f:
    for line in f:
        game_ind, game = line.split(':')
        game_splits = game.split(';')
        for split in game_splits:
            colors = split.split(',')
            for color in colors:
                nr, c = color.split()
                if int(nr) > max_for_color[c]:
                    break_flag = True
                    break
            if break_flag:
                break
        if break_flag:
            break_flag = False
            continue
    
        total += int(game_ind.split()[1])
print(total)
        