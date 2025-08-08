import sys
input = sys.stdin.readline
# 입력
n, m = map(int, input().split())
INF = float('inf')
dist = [[INF] * (n+1) for _ in range(n+1)]
for i in range(n+1): # 자기 자신은 가중치 0
    dist[i][i] = 0

for _ in range(m):
    u, v = map(int, input().split())
    dist[u][v] = dist[v][u] = 1

for k in range(1, n+1): # Floyd-Warshall
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

min_sum = sum(dist[1][1:])
min_person = 1
for i in range(2, n+1):
    cur_sum = sum(dist[i][1:])
    if cur_sum < min_sum:
        min_sum = cur_sum
        min_person = i

print(min_person)
