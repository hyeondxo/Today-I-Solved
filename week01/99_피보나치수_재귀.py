import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())

# sequence = []


def fibonacci_recursion(num):
    if num == 0:
        return []
    if num == 1:
        return [1]
    if num == 2:
        return [1, 1]
    sequence = fibonacci(num-1)
    sequence.append(sequence[-1] + sequence[-2])
    return sequence


def fibonacci(num):
    if num == 0:
        return []
    if num == 1:
        return [1]

    sequence = [1, 1]

    for i in range(2, n + 1):
        sequence.append(sequence[-1] + sequence[-2])

    return sequence


for i in fibonacci(n):
    print(f"{i} ", end="")
