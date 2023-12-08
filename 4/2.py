with open('input.txt') as f:
    lines = f.readlines()
count = [1]* len(lines)
for l_ind, line in enumerate(lines):
    hits = 0
    card, my_nrs = line.split('|')
    card_nrs = card.split(':')[1].split()
    my_nrs = my_nrs.split()
    for n in my_nrs:
        if n in card_nrs:
            hits += 1
    for i in range(hits):
        count[l_ind+i+1] +=1*count[l_ind]
print(count)
print(sum(count))
    
