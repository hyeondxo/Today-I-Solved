import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n): # floyd-warshall을 통해 모든 경로를 검사, 경로가 있다면 체크
    for i in range(n):
        if graph[i][k] == 0:
            continue
        for j in range(n):
            if not graph[i][j] and graph[k][j]:
                graph[i][j] = 1

for i in range(n):
    print(*graph[i])