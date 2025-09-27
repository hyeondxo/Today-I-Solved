import sys
input = sys.stdin.readline

n = int(input())

print(2 ** n - 1)


def solve(remain, start, temp, end):
    if remain == 1:
        print(start, end)
        return

    remain -= 1
    solve(remain, start, end, temp)
    print(start, end)
    solve(remain, temp, start, end)


if n <= 20:
    solve(n, 1, 2, 3)
