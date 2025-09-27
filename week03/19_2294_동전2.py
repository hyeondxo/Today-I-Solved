import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

def bfs():
    queue = deque([(0,0)])
    visited = [False] * (k+1)
    visited[0] = True
    while queue:
        cost, count = queue.popleft()
        for coin in coins:
            new_cost = cost + coin
            if new_cost == k:
                return count+1
            if new_cost < k and not visited[new_cost]:
                visited[new_cost] = True
                queue.append((new_cost, count + 1))
    return -1

print(bfs())