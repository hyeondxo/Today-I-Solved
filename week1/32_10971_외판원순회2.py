import sys
input = sys.stdin.readline

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

min_cost = 10 ** 9
visited = [False] * n
# city_path = []


# def calculate_cost():
#     sum = 0
#     for i in range(n-1):
#         cost = w[city_path[i]][city_path[i+1]]
#         to_start_cost = w[city_path[-1]][city_path[0]]
#         if cost == 0 or to_start_cost == 0:
#             return 10 ** 9
#         sum += cost
#     sum += to_start_cost
#     return sum


def solve(start_city, current_city, cost, depth):
    global min_cost
    if cost > min_cost:  # 비용 초과
        return

    if depth == n:
        if w[current_city][start_city] == 0:
            return
        cost += w[current_city][start_city]
        min_cost = min(min_cost, cost)
        return

    for next_city in range(n):
        if not visited[next_city] and w[current_city][next_city] != 0:
            visited[next_city] = True
            solve(start_city, next_city, cost +
                  w[current_city][next_city], depth + 1)
            visited[next_city] = False


for start_city in range(n):
    visited[start_city] = True
    solve(start_city, 0, 0, 1)
sys.stdout.write(str(min_cost))
