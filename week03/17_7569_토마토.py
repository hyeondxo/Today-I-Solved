from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque()
is_find_unripe = False
for z in range(h):
    for y in range(n):
        for x in range(m):
            cur_pos = arr[z][y][x]
            if cur_pos == 0:
                is_find_unripe = True
                continue
            if cur_pos == 1:
                queue.append((z, y, x))

if not is_find_unripe:
    print(0)
    sys.exit()

def bfs():
    while queue:
        z, y, x = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and arr[nz][ny][nx] == 0:
                arr[nz][ny][nx] = arr[z][y][x] + 1
                queue.append((nz, ny, nx))

bfs()
max_day = 0
for z in range(h):
    for y in range(n):
        for x in range(m):
            if arr[z][y][x] == 0:
                print(-1)
                sys.exit()
            max_day = max(max_day, arr[z][y][x])

print(max_day-1)

# 3차원 배열 arr
# 방향 dx, hy, dh 3가지로 검사
# 0보다 크거나같고, m(x), n(y)보다 작고, 0보다 크거나같고 h보다 작아야함
# 이 6개의 방향들만 큐에 넣어가며 일수를 하나씩 더해나감 1->2->3
# 마지막으로 전체 순회하면서 가장 높은 일수-1이 정답
# 0이 하나라도 있다면 -1출력 후 종료
