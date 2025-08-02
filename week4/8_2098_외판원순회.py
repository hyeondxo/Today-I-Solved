import sys
input = sys.stdin.readline

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * (1 << n) for _ in range(n)]

def tsp(cur, visited):
    if visited == (1 << n) - 1:
        return w[cur][0] if w[cur][0] > 0 else float("inf")
    if dp[cur][visited] != -1:
        return dp[cur][visited]
    
    cost = float('inf')
    for next in range(n):
        if not visited & (1 << next) and w[cur][next] > 0:
            next_cost = tsp(next, visited | (1 << next))
            cost = min(cost, w[cur][next] + next_cost)
    
    dp[cur][visited] = cost
    return cost

print(tsp(0, 1))
    