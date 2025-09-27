from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
max_pos = 100_000
visited = [False] * (max_pos+1)
queue = deque([(n, 0)])
while queue:
    cur, time = queue.popleft()
    if cur == k:
        print(time)
        break
    graph = [cur - 1, cur + 1, cur * 2]
    for next in graph:
        if 0 <= next <= max_pos and not visited[next]:
            visited[next] = True
            queue.append((next, time+1))
