import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
# (a ** b) % c -> ((a % c) * (b % c)) % c로 분할


def solve(a, b, c):
    if b == 1:
        return a % c
    half = solve(a, b//2, c)
    if b % 2 == 0:
        return (half * half) % c
    else:
        return (half * half * a) % c


print(int(solve(a, b, c) % c))
