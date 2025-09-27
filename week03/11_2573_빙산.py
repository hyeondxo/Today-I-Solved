import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(y, x):
    visited[y][x] = True
    melt_count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if visited[ny][nx] or nx < 0 or ny < 0 or nx >= m or ny >= n:
            continue
        if arr[ny][nx] == 0:
            melt_count += 1
    melt[y][x] += melt_count
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if arr[ny][nx] != 0 and not visited[ny][nx] and nx >= 0 and ny >= 0 and nx < m and ny < n:
            dfs(ny, nx)

year = 0
while True:
    is_all_melt = False
    is_found_iceberge = False
    visited = [[False] * m for _ in range(n)]
    melt = [[0] * m for _ in range(n)]
    for y in range(1, n-1):
        for x in range(1, m-1):
            if not visited[y][x] and arr[y][x] != 0:
                if is_found_iceberge:
                    print(year)
                    sys.exit()

                is_found_iceberge = True
                dfs(y, x)
    year += 1
    if not is_found_iceberge:
        print(0)
        sys.exit()

    for y in range(1, n-1):
        for x in range(1, m-1):
            arr[y][x] = max(0, arr[y][x] - melt[y][x])

# 모든 가능한 시작지점부터 dfs 탐색 -> 빙산 한 덩어리를 방문하고 돌아옴(상하좌우)
# dfs 이후 방문되지 않은 빙산이 있다면 빙산이 분리된 것이므로 걸린 년도를 출력 후 종료
# 종료조건은 플래그를 통해 모든 좌표가 0일 경우 다 녹았으므로 0을 출력하자.