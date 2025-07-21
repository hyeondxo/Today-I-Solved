import sys
input = sys.stdin.readline

n = int(input())
top = [n for n in map(int, input().split())]
result = [0 for _ in range(n)]
stack = []

for index in range(n):
    cur = top[index]
    while stack and stack[-1][1] <= cur:
        stack.pop()
    if stack:
        result[index] = stack[-1][0] + 1
    stack.append((index, top[index]))

sys.stdout.write(" ".join(map(str, result)))
