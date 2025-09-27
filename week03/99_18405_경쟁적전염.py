from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, target_y, target_x = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

viruses = []
for y in range(n):
    for x in range(n):
        if arr[y][x] != 0:
            viruses.append((arr[y][x], y, x, 0)) 

viruses.sort()
queue = deque(viruses)

while queue:
    type, y, x, time = queue.popleft()
    if time == s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and arr[ny][nx] == 0:
            arr[ny][nx] = type
            queue.append((type, ny, nx, time + 1))

print(arr[target_y - 1][target_x - 1])
