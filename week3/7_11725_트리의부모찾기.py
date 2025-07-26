import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

parent = [0 for _ in range(n+1)]
parent[1] = 1
visited = [False for _ in range(n+1)]


def dfs(node):
    visited[node] = True

    for next in tree[node]:
        if not visited[next]:
            parent[next] = node
            dfs(next)


dfs(1)
sys.stdout.write("\n".join(map(str, parent[2:])))
