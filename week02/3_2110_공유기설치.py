import sys
input = sys.stdin.readline

n, c = map(int, input().split())
x = [int(input()) for _ in range(n)]

x.sort()


def is_installable(distance):
    count = 1
    cur = 1
    prev = 0
    while cur < n:
        if x[cur] - x[prev] >= distance:
            count += 1
            prev = cur
            cur += 1
        else:
            cur += 1

    return count >= c


def binary_search():
    left = 0
    right = x[-1] - x[0]
    max_distance = 0

    while left <= right:
        mid = (left + right) // 2

        if (is_installable(mid)):
            max_distance = mid
            left = mid + 1
        else:
            right = mid - 1

    return max_distance


print(binary_search())
