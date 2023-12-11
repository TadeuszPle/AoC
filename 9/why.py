import sys
data = open('input3.txt').readline()
data = [int(x) for x in data.split()]
print(len(data))
print(data)
lasts = [data[-1]]
while any(data):
    
    data = [data[i+1]-data[i] for i in range(len(data)-1)]
    lasts.append(data[-1])
    print(data)
print(sum(lasts))
