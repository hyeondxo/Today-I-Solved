from collections import deque
import sys
input = sys.stdin.readline

k = int(input())
stack = deque()

for _ in range(k):
    number = int(input())
    if number == 0:
        stack.pop()
    else:
        stack.append(number)

print(sum(stack))
