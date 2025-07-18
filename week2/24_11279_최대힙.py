import heapq
import sys
input = sys.stdin.readline


n = int(input())

pq = []

for _ in range(n):
    command = int(input())
    if command == 0:
        if not pq:
            print(0)
            continue
        print(-heapq.heappop(pq))
    else:
        heapq.heappush(pq, -command)
