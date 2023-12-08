# 54967 to high
# 54253 is to high
# 54169 to low
total = 0
digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
break_flag = False
with open('input.txt', 'r') as f:
    for line in f:
        for i in range(len(line)):
            c = line[i]
            if c.isdigit():
                tens = int(c)
                break
            elif c not in ['o', 't', 'f', 's', 'e', 'n']:
                continue
            for d in range(len(digits)):
                if line[i:i+len(digits[d])] == digits[d]:
                    tens = d+1
                    break_flag = True
                    break
            if break_flag:
                break_flag = False
                break
        reversed = line[::-1]
        for i in range(len(reversed)):
            c = reversed[i]
            if c.isdigit():
                ones = int(c)
                break
            elif c not in [d[-1] for d in digits]:
                continue
            for d in range(len(digits)):
                if reversed[i:i+len(digits[d])] == digits[d][::-1]:
                    ones = d+1
                    break_flag = True
                    break
            if break_flag:
                break_flag = False
                break
        if not tens or not ones:
            print(10*tens,  ones, line[:-1])

        total = total + 10*tens + ones
        tens, ones = 0, 0

print(total)