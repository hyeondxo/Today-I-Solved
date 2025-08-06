import sys
input = sys.stdin.readline

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]
dp[0] = costs[0]

for i in range(1, n):
    # 빨강 -> 이전 집이 초록 혹은 파랑
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
    # 초록 -> 이전 집이 빨강 혹은 파랑
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
    # 파랑 -> 이전 집이 빨강 혹은 초록
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

print(min(dp[n-1]))