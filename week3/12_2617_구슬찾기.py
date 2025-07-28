import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    matrix[u][v] = 1

def floyd_warshall():
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if matrix[i][k] and matrix[k][j]:
                    matrix[i][j] = 1

floyd_warshall()
mid = (n + 1) // 2
total_count = 0
for i in range(1, n+1):
    light = 0
    heavy = 0
    for j in range(1, n+1):
        if matrix[i][j]: # i 기준, 내가 더 무거움 -> 가벼움 카운트
            light += 1
        if matrix[j][i]: # i 기준 내가 더 가벼움 -> 무거움 카운트
            heavy += 1
    if light >= mid or heavy >= mid:
        total_count += 1

print(total_count)
# 인접 행렬 만들기
# 플로이드-워셜 : i, j에 대해 k를 지나는 경로가 있으면 그 무거움/가벼움이 존재
# 마지막으로 무거움/가벼움 갯수를 세서 mid보다 크거나 같다면 중간이 될 수 없는 것
# N은 무조건 홀수임, N이 5일 때 중간 구슬은 3 -> (n+1)/2
# 앞에 2개 뒤에 2개 -> (n-1)/2
# 만약 앞 혹은 뒤에 (n+1)/2 -> 3개가 있다면 중간 구슬이 될 수 없음. 해당 구슬들을 count
