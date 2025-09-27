import sys

data = sys.stdin.read().splitlines()
n = int(data[0])
heights = list(map(int, data[1:]))
highest = heights[-1]
count = 0

for i in range(n-1, -1, -1):
    if heights[i] > highest:
        count += 1
        highest = heights[i]

print(count + 1)
