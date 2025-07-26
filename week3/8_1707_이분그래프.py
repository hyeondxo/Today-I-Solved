import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(node, color):
    visited[node] = color
    for next in graph[node]:
        if visited[next] == 0:
            if not dfs(next, -color):
                return False
        elif visited[next] == color:
            return False
    return True


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    visited = [0 for _ in range(n + 1)]
    is_bipartite = True
    for node in range(1, n+1):
        if visited[node] == 0:
            if not dfs(node, 1):
                is_bipartite = False
                break

    print("YES" if is_bipartite else "NO")
