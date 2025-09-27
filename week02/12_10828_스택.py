import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
stack = deque()


def action_command(command, val):
    if val:
        stack.append(val)
    elif command == "top":
        if not stack:
            print(-1)
            return
        print(stack[-1])
    elif command == "pop":
        if not stack:
            print(-1)
            return
        print(stack.pop())
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)


for _ in range(n):
    val = ""
    line = input().split()
    if len(line) == 2:
        command, val = line[0], line[1]
    else:
        command = line[0]

    action_command(command, val)
