from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]

visited = [[False] * (m) for _ in range(n)]
min_count = float('inf')
dy = [1, 0, 0, -1]
dx = [0, 1, -1, 0]


def bfs(x, y, cur_count):
    global min_count
    queue = deque()
    queue.append((x, y, cur_count))
    visited[y][x] = True

    while queue:
        x, y, cur_count = queue.popleft()
        if y == n-1 and x == m-1:
            min_count = min(min_count, cur_count)
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < m and ny < n and arr[ny][nx] != "0" and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((nx, ny, cur_count + 1))


bfs(0, 0, 1)
print(min_count)
