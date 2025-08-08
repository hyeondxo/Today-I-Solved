from collections import deque
import sys
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
total_count = 0

def bfs(y, x):
    global total_count
    queue = deque([(y, x)])
    visited[y][x] = True

    while queue:
        cur_y, cur_x = queue.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and arr[ny][nx] != "X":
                if arr[ny][nx] == "P":
                    total_count += 1
                queue.append((ny, nx))
                visited[ny][nx] = True
    

# 도연이의 위치로부터 탐색 시작
for y in range(n):
    for x in range(m):
        if arr[y][x] == "I":
            bfs(y, x)
            break

print("TT" if total_count == 0 else total_count)
# BFS를 통해 O를 만나면 이동가능, X나 유효하지 않은 좌표면 이동 불가
# P를 만나면 count += 1
# count = 0이면 TT 출럭