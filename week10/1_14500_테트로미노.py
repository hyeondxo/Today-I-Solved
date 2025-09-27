import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_val = max(map(max, board)) 
answer = 0

def dfs(x, y, depth, total):
    global answer
    # 가지치기
    if total + max_val * (4 - depth) <= answer:
        return
    
    if depth == 4:
        answer = max(answer, total)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth+1, total + board[nx][ny])
            visited[nx][ny] = False

def check_extra_shape(x, y):
    # ㅗ,ㅏ,ㅓ,ㅜ 모양
    global answer
    for i in range(4):
        tmp = board[x][y]
        for j in range(3):
            k = (i+j) % 4
            nx, ny = x + dx[k], y + dy[k]
            if not (0 <= nx < n and 0 <= ny < m):
                tmp = 0
                break
            tmp += board[nx][ny]
        answer = max(answer, tmp)

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False
        check_extra_shape(i, j)

print(answer)
