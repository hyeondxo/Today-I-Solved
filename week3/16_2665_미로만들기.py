import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().strip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
INF = float('inf')
dist = [[INF] * n for _ in range(n)]
dist[0][0] = 0

def dijkstra():
    min_heap = [(0, 0, 0)]
    while min_heap:
        cost, y, x = heapq.heappop(min_heap)
        if dist[y][x] < cost:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                next_cost = cost if arr[ny][nx] == 1 else cost + 1
                if next_cost < dist[ny][nx]:
                    dist[ny][nx] = next_cost
                    heapq.heappush(min_heap, (next_cost, ny, nx))

dijkstra()
print(dist[n-1][n-1])
