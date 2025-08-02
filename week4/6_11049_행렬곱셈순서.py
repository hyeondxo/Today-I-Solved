import sys
input = sys.stdin.readline

n = int(input())
matrix = [tuple(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)] # dp[i][j] = i번째 행렬부터 j번째 행렬까지 곱하는 최소 연산 횟수

for length in range(2, n+1):
    for i in range(n-length+1):
        j = i + length - 1
        dp[i][j] = float('inf')
        for k in range(i, j):
            cost = dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1]
            dp[i][j] = min(dp[i][j], cost)

print(dp[0][n-1])

# dp[0][0] = 0
# 1. 행렬 구간 i, j -> k를 기준으로 나누어 곱하기
# 2. 왼쪽 : i ~ k  -> dp[i][k] / 오른쪽 : k+1 ~ j -> dp[k+1][j]
# 3. 전체 곱셈 : 왼쪽 행 * 공통 열/행 * 오른쪽 열
# 123의 합 -> dp[i][j]
# 전체 행렬 연산 수는 맨 처음(길이가2)부터 n까지 쌓아나간 것
# 마지막 가장 긴 구간은 dp[0][n-1]