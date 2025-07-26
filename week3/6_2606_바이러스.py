import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

total_count = 0


def dfs(node):
    global total_count
    visited[node] = True

    for next in graph[node]:
        if not visited[next]:
            total_count += 1
            dfs(next)


dfs(1)
print(total_count)
