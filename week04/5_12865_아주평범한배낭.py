import sys
input = sys.stdin.readline

n, max_weight = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]
dp = [[0] * (max_weight+1) for _ in range(n+1)]

for i in range(1, n + 1):
    for cur_weight in range(1, max_weight + 1):
        weight = items[i-1][0]
        value = items[i-1][1]
        if cur_weight < weight:
            dp[i][cur_weight] = dp[i-1][cur_weight]
        else:
            dp[i][cur_weight] = max(dp[i-1][cur_weight], dp[i-1][cur_weight - weight] + value)

print(dp[n][max_weight])
