from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
start_x = start_y = 0
end_x = end_y = 0
queue = deque()

for y in range(n):
    for x in range(m):
        pos = arr[y][x]
        if pos == "*":
            queue.append((y, x, True))
        elif pos == "D":
            end_x = x
            end_y = y
        elif pos == "S":
            start_x = x
            start_y = y

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dist = [[0] * m for _ in range(n)]
dist[start_y][start_x] = 1

def bfs():
    queue.append((start_y, start_x, False))
    while queue:
        y, x, is_water = queue.popleft()
        if is_water:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and arr[ny][nx] == ".":
                    arr[ny][nx] = "*"
                    queue.append((ny, nx, True))
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and arr[ny][nx] not in ("*", "X") and arr[ny][nx] in ("D", "."):
                    if dist[ny][nx] == 0:
                        dist[ny][nx] = dist[y][x] + 1
                        queue.append((ny, nx, False))

bfs()
print(dist[end_y][end_x]-1 if dist[end_y][end_x] > 0 else "KAKTUS")
# 물 먼저 이동
# 고슴도치 이동 -> 이동 좌표마다 시간 +1
# dist[end_x][end_y]가 정답. 0이면 KAKTUS