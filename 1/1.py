total_sum = 0
with open('input.txt', 'r') as f:
    for line in f:
        for c in line:
            if c.isdigit():
                tens = int(c)
                break
        for c in line[::-1]:
            if c.isdigit():
                ones = int(c)
                break
        total_sum = total_sum + 10*tens + ones
print(total_sum)

