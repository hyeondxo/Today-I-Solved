import sys
input = sys.stdin.readline

n = int(input())


def fibonacci(number):
    if number < 0:
        return []
    if number == 0:
        return 0
    if number == 1:
        return 1

    prev = 0
    cur = 1
    for _ in range(2, n + 1):
        prev, cur = cur, prev + cur

    return cur


print(fibonacci(n))
