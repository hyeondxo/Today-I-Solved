import sys
input = sys.stdin.readline

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
city_path = []
min_cost = 10 ** 9


def calculateCost():
    sum = 0
    for i in range(n-1):
        cost = w[city_path[i]][city_path[i+1]]
        to_start_cost = w[city_path[-1]][city_path[0]]
        if cost == 0 or to_start_cost == 0:
            return 10 ** 9
        sum += cost
    sum += to_start_cost
    return sum


def backtracking():
    if len(city_path) == n:
        global min_cost
        min_cost = min(min_cost, calculateCost())
        return

    for i in range(0, n):
        if visited[i]:
            continue
        visited[i] = True
        city_path.append(i)
        backtracking()
        visited[i] = False
        city_path.pop()


backtracking()
print(min_cost)
