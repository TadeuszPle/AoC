with open('input.txt') as f:
    lines = f.readlines()
times, distances = lines
times = map(int,times.split(':')[1].strip().split())
distances = map(int,distances.split(':')[1].strip().split())
out = 1
for time, dist in zip(times, distances):
    cur = 0
    for x in range(time):
        if x*(time - x) > dist:
            cur += 1
    out = out * cur
print(out)

