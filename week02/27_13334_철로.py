import heapq as hq
import sys
input = sys.stdin.readline

n = int(input())
position = []
for _ in range(n):
    x, y = map(int, input().split())
    if x > y:
        position.append((y, x))
    else:
        position.append((x, y))
d = int(input())
position.sort(key=lambda x: (x[1], x[0]))

l = []
cur_len = 0
max_count = 0
for x, y in position:
    hq.heappush(l, (x, y))
    cur_len += 1
    end = y

    while (y - l[0][0]) > d:
        hq.heappop(l)
        cur_len -= 1
        if cur_len == 0:
            break
    max_count = max(max_count, cur_len)

print(max_count)
