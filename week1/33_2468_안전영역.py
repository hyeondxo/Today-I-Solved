from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]
max_height = max(max(row) for row in area)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(y, x, visited, rained):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and ny >= 0 and nx < n and ny < n:
                if not visited[ny][nx] and area[ny][nx] > rained:
                    visited[ny][nx] = True
                    queue.append((nx, ny))


max_count = 0
for rained in range(0, max_height + 1):
    visited = [[False]*n for _ in range(n)]
    count = 0
    for y in range(n):
        for x in range(n):
            if area[y][x] > rained and not visited[y][x]:
                bfs(y, x, visited, rained)
                count += 1

    max_count = max(count, max_count)

print(max_count)
