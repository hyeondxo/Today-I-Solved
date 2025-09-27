import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
total_count = 0

def dfs(y, x, style):
    global total_count
    visited[y][x] = True
    if style == "-":
        nx = x + 1
        if nx < m and not visited[y][nx] and style == arr[y][nx]:
            dfs(y, nx, style)
    else:
        ny = y + 1
        if ny < n and not visited[ny][x] and style == arr[ny][x]:
            dfs(ny, x, style)

for y in range(n):
    for x in range(m):
        if not visited[y][x]:
            dfs(y, x, arr[y][x])
            total_count += 1

print(total_count)
