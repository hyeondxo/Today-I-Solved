from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()


def dfs(v, visited_dfs):
    visited_dfs[v] = True
    print(v, end=" ")
    for next in graph[v]:
        if not visited_dfs[next]:
            dfs(next, visited_dfs)


def bfs(start):
    queue = deque([start])
    visited_bfs = [False for _ in range(n+1)]
    visited_bfs[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for next in graph[v]:
            if not visited_bfs[next]:
                visited_bfs[next] = True
                queue.append(next)


visited_dfs = [False for _ in range(n+1)]
dfs(v, visited_dfs)
print()
bfs(v)
