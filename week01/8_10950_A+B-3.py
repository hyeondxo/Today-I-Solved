import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n1, n2 = map(int, input().split())
    print(n1 + n2)
