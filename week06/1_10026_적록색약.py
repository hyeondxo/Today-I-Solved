from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input().strip()) for _ in range(n)]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
visited_norm = [[False] * n for _ in range(n)] 
visited_cb   = [[False] * n for _ in range(n)]  

def bfs(y, x):
    start = arr[y][x]
    allow_norm = {start}
    allow_cb = {'B'} if start == 'B' else {'R', 'G'}

    q = deque()

    started_norm = False
    started_cb   = False

    if not visited_norm[y][x]:
        visited_norm[y][x] = True
        q.append((y, x, 0)) # mode 0 : 정상
        started_norm = True
    if not visited_cb[y][x]:
        visited_cb[y][x] = True
        q.append((y, x, 1)) # mode 1 : 색약
        started_cb = True

    while q:
        cy, cx, mode = q.popleft()
        for k in range(4):
            ny, nx = cy + dy[k], cx + dx[k]
            if not (0 <= ny < n and 0 <= nx < n):
                continue
            if mode == 0: # 정상 모드
                if not visited_norm[ny][nx] and arr[ny][nx] in allow_norm:
                    visited_norm[ny][nx] = True
                    q.append((ny, nx, 0))
            else: # 색약 모드
                if not visited_cb[ny][nx] and arr[ny][nx] in allow_cb:
                    visited_cb[ny][nx] = True
                    q.append((ny, nx, 1))

    return started_norm, started_cb

normal_count = 0
cb_count = 0

for y in range(n):
    for x in range(n):
        if visited_norm[y][x] and visited_cb[y][x]:
            continue
        sn, sc = bfs(y, x)
        if sn: normal_count += 1   
        if sc: cb_count     += 1  

print(normal_count, cb_count)