import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    graph[parent].append((child, weight))
    graph[child].append((parent, weight))

def dfs(node, weight):
    for next_node, next_weight in graph[node]:
        if distance[next_node] == -1:
            new_weight = weight + next_weight
            distance[next_node] = new_weight
            dfs(next_node, new_weight)

distance = [-1] * (n+1)
distance[1] = 0
dfs(1, 0)

start = distance.index(max(distance))
distance = [-1] * (n+1)
distance[start] = 0
dfs(start, 0)
print(max(distance))