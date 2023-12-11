# i like this approach because we can apply binary search to find the first pascal line that gives us all zero
# the problem is that it works but would break for certain valid inputs: if i get a line like [4, 4, 10, 14, 16, 16] it would break

# couldn't understant how i am off by 2 in line 99 when i didnt check the first element
# with brute force approach: 
# [4, 10, 14, 16, 16]
# [6, 4, 2, 0] <- here the last element is zero but first is not
# [-2, -2, -2]
# [0, 0]
# 8915409
# my ans = 8915411
import sys
from functools import reduce
data = open(sys.argv[1]).readlines()
lines = [list(map(int,line.strip().split())) for line in data]

def pascal_triangle(n) -> list[int]:
    if n == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal_triangle(n-1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
    return line


for part2 in [False, True]:
    sums = []
    for line in lines:
        for i in range(2,len(line)+1):
            triangle = pascal_triangle(i)
            triangle_altering = [p*((-1)**j) for j,p in enumerate(triangle)]
            zipped = zip(triangle_altering,line[::-1])
            summed = reduce(lambda acum,x: acum+x[0]*x[1], zipped, 0)
            if summed == 0:
                # this means that the last element is 0:
                # now we need to check for the first element
                check_first = reduce(lambda acum,x: acum+x[0]*x[1],zip(triangle_altering, line), 0)
                if check_first:
                    continue
                next_triangle = [1] + [triangle[i] + triangle[i+1] for i in range(len(triangle)-1)] + [1]
                next_triangle_altering = [p*((-1)**(j)) for j,p in enumerate(next_triangle)]
                
                if part2:
                    zipped_next = zip(next_triangle_altering[1:],line)
                    summed = -reduce(lambda acum,x: acum+x[0]*x[1], zipped_next, 0)
                else:    
                    zipped_next = zip(next_triangle_altering[1:],line[::-1])
                    summed = -reduce(lambda acum,x: acum+x[0]*x[1], zipped_next, 0)

                sums.append(summed)
                break
    print(sum(sums))
# too high: 1916822652
# too high: 10933517378
            