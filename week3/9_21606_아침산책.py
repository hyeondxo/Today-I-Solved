from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
inside = "0" + input().strip()
graph = [[] for _ in range(n+1)]
total_count = 0
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    if inside[u] == "1" and inside[v] == "1":
        total_count += 2

visited = [False for _ in range(n+1)]


def dfs(start):
    visited[start] = True
    inside_count = 0
    for next in graph[start]:
        if inside[next] == "1":
            inside_count += 1
        elif not visited[next] and inside[next] == "0":
            inside_count += dfs(next)
    return inside_count


for start in range(1, n+1):
    if inside[start] == "0" and not visited[start]:
        count = dfs(start)
        total_count += count * (count - 1)

print(total_count)
