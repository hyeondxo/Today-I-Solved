import heapq as hq
import sys
input = sys.stdin.readline

n = int(input())
min_heap = []
max_heap = []
init = int(input())

hq.heappush(min_heap, -init)
min_size = 1
max_size = 0
print(init)

for _ in range(1, n):
    num = int(input())

    if min_size > max_size:
        if -min_heap[0] > num:
            hq.heappush(max_heap, -hq.heappop(min_heap))
            hq.heappush(min_heap, -num)
        else:
            hq.heappush(max_heap, num)
        max_size += 1
        print(-min_heap[0])
    else:
        if max_heap[0] > num:
            hq.heappush(min_heap, -num)
        else:
            hq.heappush(min_heap, -hq.heappop(max_heap))
            hq.heappush(max_heap, num)
        min_size += 1
        print(-min_heap[0])
