from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [-1] * (n+1)
distance[x] = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)


def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        cur = queue.popleft()
        for next in graph[cur]:
            if distance[next] == -1:
                distance[next] = distance[cur]+1
                queue.append(next)


bfs(x)
found = False

for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        found = True
if not found:
    print(-1)
