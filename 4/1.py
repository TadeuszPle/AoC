total = 0
with open('input.txt') as f:
    for line in f:
        val = 0
        card, my_nrs = line.split('|')
        card_nrs = card.split(':')[1].split()
        my_nrs = my_nrs.split()
        for n in my_nrs:
            if n in card_nrs:
                if not val:
                    val = 1
                else:
                    val *= 2
        total += val
print(total)