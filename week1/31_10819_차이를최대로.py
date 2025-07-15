import sys
input = sys.stdin.readline

n = int(input())
arr = list(map, int(input().split()))
visited = [False] * n

cur_max = 0


def calculateSum(cur_arr):
    sum = 0
    for i in range(n-1):
        sum += abs(cur_arr[i] - cur_arr[i + 1])
    return sum


def backtracking(cur_arr: list):
    if (len(cur_arr) == n):
        new_max = calculateSum(cur_arr)
        global cur_max
        cur_max = max(new_max, cur_max)
        return

    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        cur_arr.append(arr[i])
        backtracking(cur_arr)
        visited[i] = False
        cur_arr.pop()


backtracking([])
print(cur_max)
