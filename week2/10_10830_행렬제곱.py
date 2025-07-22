import sys
input = sys.stdin.readline

n, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


def power(arr, b):
    if b == 1:
        return [[num % 1000 for num in row] for row in arr]

    half = power(arr, b // 2)

    if b % 2 == 0:
        return arr_mul(half, half)
    else:
        return arr_mul(arr_mul(half, half), arr)


def arr_mul(arr1, arr2):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += arr1[i][k] * arr2[k][j]
            result[i][j] %= 1000

    return result


result = power(arr, b)

for row in result:
    print(*row)
