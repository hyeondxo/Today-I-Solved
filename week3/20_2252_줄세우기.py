from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    indegree[v] += 1

result = []
def topology_sort():
    queue = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        cur = queue.popleft()
        result.append(cur)
        for next in graph[cur]:
            indegree[next] -= 1
            if indegree[next] == 0:
                queue.append(next)

topology_sort()
print(*result)