import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
reverse_graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
dist = [0] * (n+1)

for _ in range(m):
    u, v , cost = map(int, input().split())
    graph[u].append((v, cost))
    reverse_graph[v].append((u, cost))
    indegree[v] += 1

start, end = map(int, input().split())

queue = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    cur = queue.popleft()
    for next, time in graph[cur]:
        dist[next] = max(dist[next], dist[cur]+time)
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)

print(dist[end])

visited = [False] * (n+1)
queue = deque([end])
count = 0
while queue:
    last = queue.popleft()
    for prev, time in reverse_graph[last]:
        if dist[last] == dist[prev]+time:
            count += 1
            if not visited[prev]:
                visited[prev] = True
                queue.append(prev)
                
                
print(count)