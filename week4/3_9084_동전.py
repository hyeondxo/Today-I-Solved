import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    cost = int(input())

    dp = [0] * (cost + 1) # dp[i] = i원을 만들 수 있는 모든 방법의 수
    dp[0] = 1
    for coin in coins:
        for cur_cost in range(cost + 1):
            if coin <= cur_cost:
                dp[cur_cost] += dp[cur_cost - coin]

    print(dp[cost])