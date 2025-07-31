import sys
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(1)
    sys.exit()
if n == 2:
    print(2)
    sys.exit()

dp = [0] * (n+1)
dp[1] = 1 # 1
dp[2] = 2 # 11, 00
# dp[3] = 3 -> 111, 100, 001
for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[n])

# 타일의 경우의 수는 1 또는 00
# 마지막을 1로 두면 그 앞까지 만들 수 있는 경우의 수는 N-1
# 마지막을 00으로 두면 그 앞까지 만들 수 있는 경우의 수는 N-2
# 마지막을 1 또는 00으로 두는 경우의 수는 N-1 + N-2
